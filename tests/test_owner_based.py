import pytest
from web3 import Web3
from solcx import compile_source, install_solc, set_solc_version

# Устанавливаем компилятор Solidity 0.8.0
install_solc('0.8.0')
set_solc_version('0.8.0')

# Исходный код контракта OwnerBasedStorage.sol
contract_source_owner = """
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract OwnerBasedStorage {
    address public owner;
    uint256 private storedData;

    event DataSet(address indexed setter, uint256 value);

    constructor() {
        owner = msg.sender;
    }

    function set(uint256 _data) public {
        require(msg.sender == owner, "Only owner can set the data");
        storedData = _data;
        emit DataSet(msg.sender, _data);
    }

    function get() public view returns (uint256) {
        return storedData;
    }
}
"""

@pytest.fixture
def w3():
    """Создаем локальный Web3 провайдер, подключенный к Ganache"""
    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    w3.eth.default_account = w3.eth.accounts[0]
    return w3

@pytest.fixture
def owner_based_contract(w3):
    """Компилируем и разворачиваем контракт OwnerBasedStorage"""
    compiled_sol = compile_source(contract_source_owner, solc_version="0.8.0")
    contract_interface = compiled_sol['<stdin>:OwnerBasedStorage']

    OwnerBasedStorage = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']
    )
    tx_hash = OwnerBasedStorage.constructor().transact({'from': w3.eth.default_account, 'gas': 3000000})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return w3.eth.contract(
        address=tx_receipt.contractAddress,
        abi=contract_interface['abi']
    )

def test_deployment(owner_based_contract, w3):
    # Проверяем, что владелец контракта совпадает с w3.eth.accounts[0]
    contract_owner = owner_based_contract.functions.owner().call()
    assert contract_owner == w3.eth.accounts[0]

def test_set_by_owner(owner_based_contract, w3):
    # Тест: владелец может установить значение
    tx_hash = owner_based_contract.functions.set(123).transact({
        'from': w3.eth.default_account,
        'gas': 3000000
    })
    w3.eth.wait_for_transaction_receipt(tx_hash)
    value = owner_based_contract.functions.get().call()
    assert value == 123

def test_set_by_non_owner(owner_based_contract, w3):
    # Тест: если вызов происходит от не владельца, транзакция откатывается
    with pytest.raises(Exception) as excinfo:
        tx_hash = owner_based_contract.functions.set(999).transact({
            'from': w3.eth.accounts[1],
            'gas': 3000000
        })
        w3.eth.wait_for_transaction_receipt(tx_hash)
    assert "Only owner can set the data" in str(excinfo.value)

def test_event_emission(owner_based_contract, w3):
    # Тест: при успешном вызове функции set() должно сгенерироваться событие DataSet
    tx_hash = owner_based_contract.functions.set(777).transact({
        'from': w3.eth.default_account,
        'gas': 3000000
    })
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    logs = owner_based_contract.events.DataSet().process_receipt(receipt)
    assert len(logs) == 1
    event_args = logs[0]['args']
    assert event_args['setter'] == w3.eth.accounts[0]
    assert event_args['value'] == 777
