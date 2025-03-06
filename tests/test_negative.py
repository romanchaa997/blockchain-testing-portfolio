import pytest
from web3 import Web3
from solcx import compile_source, install_solc, set_solc_version

#Install and set up the Solidity compiler version 0.8.0
install_solc('0.8.0')
set_solc_version('0.8.0')

# Source code of the contract with restriction
contract_source_v2 = """
pragma solidity ^0.8.0;

contract SimpleStorageV2 {
    uint256 private storedData;

    function set(uint256 _data) public {
        require(_data <= 1000, "Value too high");
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
def contract_v2(w3):
    """Compile and deploy the contract SimpleStorageV2"""
    compiled_sol = compile_source(contract_source_v2, solc_version="0.8.0")
    contract_interface = compiled_sol['<stdin>:SimpleStorageV2']

    SimpleStorageV2 = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']
    )
    tx_hash = SimpleStorageV2.constructor().transact({'from': w3.eth.default_account, 'gas':3000000})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return w3.eth.contract(
        address=tx_receipt.contractAddress,
        abi=contract_interface['abi']
    )

def test_set_too_high(contract_v2, w3):
    """We check that when trying to set a value greater than 1000, the transaction is rolled back"""
    with pytest.raises(Exception) as excinfo:
        tx_hash = contract_v2.functions.set(2000).transact({'from': w3.eth.default_account, 'gas':3000000})
        w3.eth.wait_for_transaction_receipt(tx_hash)
    # Let's make sure the error message contains "Value too high"
    assert "Value too high" in str(excinfo.value)
