import pytest
from web3 import Web3

@pytest.fixture
def infura_w3():
    #Replace the URL with your Infura endpoint for Sepolia
    infura_url = "https://sepolia.infura.io/v3/3bcddb4bb74f41cfa07202d3c77b1c1c"
    w3 = Web3(Web3.HTTPProvider(infura_url))
    assert w3.is_connected(), "Failed to connect to Infura"
    return w3

def test_infura_connection(infura_w3):
    # We get the current block number
    block_number = infura_w3.eth.block_number
    print("Текущий номер блока:", block_number)
    # We check that blocks have already been accumulated (for example, that the number is greater than 0)
    assert isinstance(block_number, int) and block_number > 0, "The block number must be a positive integer."
