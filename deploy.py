import os
print("INFURA_URL:", os.environ.get("INFURA_URL"))
print("DEPLOYER_PRIVATE_KEY:", os.environ.get("DEPLOYER_PRIVATE_KEY"))

import os
from web3 import Web3
from solcx import compile_source, install_solc, set_solc_version

# Installing the Solidity compiler
install_solc('0.8.0')
set_solc_version('0.8.0')

# Loading Infura API Key and Private Key from Environment Variables
INFURA_URL = os.environ.get("INFURA_URL")
PRIVATE_KEY = os.environ.get("DEPLOYER_PRIVATE_KEY")

# Example of contract source code (can be replaced with the required contract)
contract_source_code = '''
// SPDX-License-Identifier: MIT
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
'''

def deploy_contract():
    w3 = Web3(Web3.HTTPProvider(INFURA_URL))
    # Obtain the deployment address from the private key
    account = w3.eth.account.from_key(PRIVATE_KEY)
    deployer_address = account.address
    print("Deployer address:", deployer_address)

    # Compiling the contract
    compiled_sol = compile_source(contract_source_code, solc_version="0.8.0")
    contract_id, contract_interface = compiled_sol.popitem()

    # We are creating a contract factory
    SimpleStorage = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

    # Forming a transaction
    construct_txn = SimpleStorage.constructor().build_transaction({
        'from': deployer_address,
        'nonce': w3.eth.get_transaction_count(deployer_address),
        'gas': 3000000,
        'gasPrice': w3.to_wei('10', 'gwei')
    })

    # We sign the transaction
    signed_txn = w3.eth.account.sign_transaction(construct_txn, private_key=PRIVATE_KEY)

    # Sending a transaction
    tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
    print("Deploying contract, tx hash:", tx_hash.hex())

    # We are waiting for confirmation
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Contract deployed at address:", tx_receipt.contractAddress)

if __name__ == "__main__":
    deploy_contract()
