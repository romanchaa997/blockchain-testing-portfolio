import pytest
from web3 import Web3

def test_reentrancy_attack(w3, vulnerable_contract, attacker_contract):
    # Депозит 1 ETH от жертвы
    tx = vulnerable_contract.functions.deposit().transact({'from': w3.eth.accounts[1], 'value': Web3.toWei(1, 'ether')})
    w3.eth.wait_for_transaction_receipt(tx)

    # Атака: вызов withdraw() через зловредный контракт
    tx = attacker_contract.functions.attack().transact({'from': w3.eth.accounts[2]})
    w3.eth.wait_for_transaction_receipt(tx)

    # Проверяем баланс контракта – он должен быть опустошен
    assert w3.eth.get_balance(vulnerable_contract.address) == 0
