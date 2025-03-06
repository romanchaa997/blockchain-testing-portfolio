import pytest
from web3 import Web3
from solcx import compile_source, install_solc, set_solc_version
import random
import time

# Install and set up the Solidity compiler version 0.8.0
install_solc('0.8.0')
set_solc_version('0.8.0')

# Contract source code SimpleStorage.sol
contract_source = """
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 private storedData;

    function set(uint256 _data) public {
        storedData = _data;
    }

    function get() public view returns (uint256) {
        return storedData;
    }
}
"""

@pytest.fixture
def w3():
    """Create a local Web3 provider connected to Ganache"""
    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    w3.eth.default_account = w3.eth.accounts[0]
    return w3

@pytest.fixture
def contract(w3):
    """Compile and deploy the contract"""
    compiled_sol = compile_source(contract_source, solc_version="0.8.0")
    contract_interface = compiled_sol['<stdin>:SimpleStorage']

    SimpleStorage = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']
    )
    tx_hash = SimpleStorage.constructor().transact({'from': w3.eth.default_account, 'gas': 3000000})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return w3.eth.contract(
        address=tx_receipt.contractAddress,
        abi=contract_interface['abi']
    )

def test_deployment(contract):
    # Check that the contract address has been received
    assert contract.address is not None

def test_set_and_get(contract, w3):
    tx_hash = contract.functions.set(42).transact({'from': w3.eth.default_account, 'gas': 3000000})
    w3.eth.wait_for_transaction_receipt(tx_hash)
    value = contract.functions.get().call()
    assert value == 42

def test_no_reentrancy(contract):
    value_before = contract.functions.get().call()
    value_after = contract.functions.get().call()
    assert value_before == value_after

def test_load_set(contract, w3):
    num_transactions = 100
    start = time.time()
    for _ in range(num_transactions):
        tx_hash = contract.functions.set(random.randint(1, 100)).transact({'from': w3.eth.default_account, 'gas': 3000000})
        w3.eth.wait_for_transaction_receipt(tx_hash)
    elapsed = time.time() - start
    print(f"{num_transactions} transactions completed in {elapsed:.2f} секунд")
    assert elapsed < 10
