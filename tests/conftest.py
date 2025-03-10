import pytest
from web3 import Web3

@pytest.fixture(scope="module")
def w3():
    # Підключення до локального блокчейну через Ganache або Anvil
    provider = Web3.HTTPProvider('http://127.0.0.1:8545')
    w3 = Web3(provider)
    assert w3.is_connected(), "Failed to connect to the blockchain"
    return w3
