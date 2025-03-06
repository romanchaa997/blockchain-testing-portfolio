import pytest
from web3 import Web3
from solcx import compile_source, install_solc, set_solc_version
import time

# Install Solidity compiler version 0.8.0
install_solc('0.8.0')
set_solc_version('0.8.0')

# AdvancedStorage Contract Source Code
contract_source_code = '''
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AdvancedStorage {
    uint256 private storedData;

    event DataSet(address indexed setter, uint256 value);

    function set(uint256 _data) public {
        require(_data <= 1000, "Value too high");
        storedData = _data;
        emit DataSet(msg.sender, _data);
    }

    function get() public view returns (uint256) {
        return storedData;
    }
}
'''

@pytest.fixture
def w3():
    """Create a local Web3 provider (Ganache)"""
    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    w3.eth.default_account = w3.eth.accounts[0]
    return w3

@pytest.fixture
def advanced_contract(w3):
    """Compile and deploy the contract AdvancedStorage"""
    compiled_sol = compile_source(contract_source_code, solc_version="0.8.0")
    contract_interface = compiled_sol['<stdin>:AdvancedStorage']
    AdvancedStorage = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']
    )
    tx_hash = AdvancedStorage.constructor().transact({'from': w3.eth.default_account, 'gas': 3000000})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return w3.eth.contract(
        address=tx_receipt.contractAddress,
        abi=contract_interface['abi']
    )

# Functional test: correct value update
def test_advanced_set_get(advanced_contract, w3):
    tx_hash = advanced_contract.functions.set(500).transact({
        'from': w3.eth.default_account,
        'gas': 3000000
    })
    w3.eth.wait_for_transaction_receipt(tx_hash)
    value = advanced_contract.functions.get().call({'from': w3.eth.default_account})
    assert value == 500

# Negative test: attempt to set invalid value
def test_advanced_set_invalid(advanced_contract, w3):
    with pytest.raises(Exception) as excinfo:
        tx_hash = advanced_contract.functions.set(1500).transact({
            'from': w3.eth.default_account,
            'gas': 3000000
        })
        w3.eth.wait_for_transaction_receipt(tx_hash)
    assert "Value too high" in str(excinfo.value)

# Load test: calling a function multiple times set()
def test_load_advanced_set(advanced_contract, w3):
    num_calls = 100
    for i in range(num_calls):
        tx_hash = advanced_contract.functions.set(i).transact({
            'from': w3.eth.default_account,
            'gas': 3000000
        })
        w3.eth.wait_for_transaction_receipt(tx_hash)
    # The last call should set the value num_calls - 1
    value = advanced_contract.functions.get().call({'from': w3.eth.default_account})
    assert value == num_calls - 1

# Integration test: deploy to a live network via Infura
# This test will be skipped if the account does not have enough funds.
@pytest.mark.skip(reason="Real network deployment test skipped due to insufficient funds")
def test_deployment_real_network():
    # This test can be implemented similarly to yours deploy.py
    pass

# Integration Test: Checking Connection with Infura
@pytest.mark.skip(reason="Integration test skipped due to insufficient funds")
def test_infura_connection(w3):
    block_number = w3.eth.block_number
    assert block_number > 0
