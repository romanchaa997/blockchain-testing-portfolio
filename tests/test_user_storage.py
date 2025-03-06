import pytest
from web3 import Web3
from solcx import compile_source, install_solc, set_solc_version

# Install and configure the Solidity 0.8.0 compiler
install_solc('0.8.0')
set_solc_version('0.8.0')

# Contract source code UserStorage
contract_source_user = """
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract UserStorage {
    mapping(address => uint256) private data;
    
    event DataUpdated(address indexed user, uint256 newValue);
    
    function set(uint256 _data) public {
        data[msg.sender] = _data;
        emit DataUpdated(msg.sender, _data);
    }
    
    function get() public view returns (uint256) {
        return data[msg.sender];
    }
    
    function getFor(address _user) public view returns (uint256) {
        return data[_user];
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
def user_storage_contract(w3):
    """Compile and deploy the contract UserStorage"""
    compiled_sol = compile_source(contract_source_user, solc_version="0.8.0")
    contract_interface = compiled_sol['<stdin>:UserStorage']
    
    UserStorage = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']
    )
    tx_hash = UserStorage.constructor().transact({'from': w3.eth.default_account, 'gas': 3000000})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return w3.eth.contract(
        address=tx_receipt.contractAddress,
        abi=contract_interface['abi']
    )

def test_self_set_get(user_storage_contract, w3):
    """Check: user can set and get their own value."""
# Set value 555 on behalf accounts[0]
    tx_hash = user_storage_contract.functions.set(555).transact({
        'from': w3.eth.default_account,
        'gas': 3000000
    })
    w3.eth.wait_for_transaction_receipt(tx_hash)
    # Check that the get() function returns 555
    value = user_storage_contract.functions.get().call({'from': w3.eth.default_account})
    assert value == 555

def test_independent_storage(user_storage_contract, w3):
    """Independent storage check: different accounts store their own values."""
    # accounts[0] sets the value 100
    tx_hash0 = user_storage_contract.functions.set(100).transact({
        'from': w3.eth.accounts[0],
        'gas': 3000000
    })
    w3.eth.wait_for_transaction_receipt(tx_hash0)
    # accounts[1] sets the value 200
    tx_hash1 = user_storage_contract.functions.set(200).transact({
        'from': w3.eth.accounts[1],
        'gas': 3000000
    })
    w3.eth.wait_for_transaction_receipt(tx_hash1)
    # Check that the values ​​are stored independently
    value0 = user_storage_contract.functions.getFor(w3.eth.accounts[0]).call()
    value1 = user_storage_contract.functions.getFor(w3.eth.accounts[1]).call()
    assert value0 == 100
    assert value1 == 200

def test_event_emission_user(user_storage_contract, w3):
    """Check: When calling the set() function, an event is generated DataUpdated."""
    tx_hash = user_storage_contract.functions.set(777).transact({
        'from': w3.eth.accounts[2],
        'gas': 3000000
    })
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    logs = user_storage_contract.events.DataUpdated().process_receipt(receipt)
    assert len(logs) == 1
    event_args = logs[0]['args']
    assert event_args['user'] == w3.eth.accounts[2]
    assert event_args['newValue'] == 777
