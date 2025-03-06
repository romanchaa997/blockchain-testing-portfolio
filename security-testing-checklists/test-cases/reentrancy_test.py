import pytest
from web3 import Web3

def test_reentrancy_attack(w3, vulnerable_contract, attacker_contract):
    # Deposit 1 ETH from the victim
    tx = vulnerable_contract.functions.deposit().transact({'from': w3.eth.accounts[1], 'value': Web3.toWei(1, 'ether')})
    w3.eth.wait_for_transaction_receipt(tx)

    # Attack: Calling withdraw() via a malicious contract
    tx = attacker_contract.functions.attack().transact({'from': w3.eth.accounts[2]})
    w3.eth.wait_for_transaction_receipt(tx)

    # We check the contract balance - it should be empty
    assert w3.eth.get_balance(vulnerable_contract.address) == 0
