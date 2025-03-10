import pytest
from web3 import Web3
from solcx import compile_source

# Вкажи ABI і Bytecode контракту
CONTRACT_SOURCE_CODE = '''
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ReentrancyAttack {
    mapping(address => uint256) public balances;

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
        balances[msg.sender] -= amount;
    }

    receive() external payable {
        if (address(this).balance > 0) {
            withdraw(address(this).balance);
        }
    }
}
'''

@pytest.fixture
def contract(w3):
    compiled = compile_source(CONTRACT_SOURCE_CODE)
    contract_interface = compiled['<stdin>:ReentrancyAttack']
    
    tx_hash = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']
    ).constructor().transact({'from': w3.eth.accounts[0]})
    
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return w3.eth.contract(
        address=tx_receipt.contractAddress,
        abi=contract_interface['abi']
    )

def test_reentrancy_attack(w3, contract):
    attacker = w3.eth.accounts[1]
    owner = w3.eth.accounts[0]

    # Депозит власником контракту
    contract.functions.deposit().transact({'from': owner, 'value': w3.to_wei(1, 'ether')})

    # Перевірка балансу
    assert contract.functions.balances(owner).call() == w3.to_wei(1, 'ether')

    # Виконання атаки Reentrancy
    with pytest.raises(Exception):
        contract.functions.withdraw(w3.to_wei(1, 'ether')).transact({'from': attacker})

    # Перевіряємо, що баланс залишився незмінним після невдалої атаки
    assert contract.functions.balances(owner).call() == w3.to_wei(1, 'ether')
