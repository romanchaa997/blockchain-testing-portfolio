import time
import pytest
from web3 import Web3
from solcx import compile_source, install_solc, set_solc_version

# Ensure the correct Solidity compiler is used.
install_solc('0.8.0')
set_solc_version('0.8.0')

# AdvancedStorage contract source code
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
    """Compile and deploy the AdvancedStorage contract"""
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

def test_stress_set(advanced_contract, w3):
    """Stress test: perform 1000 calls to the set() function and measure execution time."""
    num_calls = 1000
    start_time = time.time()
    for i in range(num_calls):
        tx_hash = advanced_contract.functions.set(i % 1000).transact({'from': w3.eth.default_account, 'gas': 3000000})
        w3.eth.wait_for_transaction_receipt(tx_hash)
    elapsed = time.time() - start_time
    print(f"Executed {num_calls} calls in {elapsed:.2f} seconds")
    # Ensure the final value is as expected.
    final_value = advanced_contract.functions.get().call({'from': w3.eth.default_account})
    assert final_value == (num_calls - 1) % 1000
