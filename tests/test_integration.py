import pytest
from web3 import Web3

@pytest.fixture
def infura_w3():
    # Замените URL на ваш Infura endpoint для Sepolia
    infura_url = "https://sepolia.infura.io/v3/3bcddb4bb74f41cfa07202d3c77b1c1c"
    w3 = Web3(Web3.HTTPProvider(infura_url))
    assert w3.is_connected(), "Не удалось подключиться к Infura"
    return w3

def test_infura_connection(infura_w3):
    # Получаем текущий номер блока
    block_number = infura_w3.eth.block_number
    print("Текущий номер блока:", block_number)
    # Проверяем, что блоков уже накоплено (например, что номер больше 0)
    assert isinstance(block_number, int) and block_number > 0, "Номер блока должен быть положительным целым числом"
