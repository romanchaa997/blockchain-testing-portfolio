import pytest
from web3 import Web3

def test_front_running_attack(w3, dex_contract, attacker_contract):
    tx_victim = dex_contract.functions.swap(Web3.toWei(1, 'ether')).transact({'from': w3.eth.accounts[1]})
    tx_attacker = dex_contract.functions.swap(Web3.toWei(1, 'ether')).transact({
        'from': w3.eth.accounts[2], 
        'gasPrice': w3.eth.gas_price + 1000000000
    })
    
    receipt_victim = w3.eth.get_transaction_receipt(tx_victim)
    receipt_attacker = w3.eth.get_transaction_receipt(tx_attacker)

    assert receipt_attacker.blockNumber < receipt_victim.blockNumber
