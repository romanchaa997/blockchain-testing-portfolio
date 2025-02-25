import os
print("INFURA_URL:", os.environ.get("INFURA_URL"))
print("DEPLOYER_PRIVATE_KEY:", os.environ.get("DEPLOYER_PRIVATE_KEY"))

import os
from web3 import Web3
from solcx import compile_source, install_solc, set_solc_version

# Устанавливаем компилятор Solidity
install_solc('0.8.0')
set_solc_version('0.8.0')

# Загрузка API ключа Infura и приватного ключа из переменных среды
INFURA_URL = os.environ.get("INFURA_URL")
PRIVATE_KEY = os.environ.get("DEPLOYER_PRIVATE_KEY")

# Пример исходного кода контракта (можно заменить на нужный контракт)
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
    # Получаем адрес развертывания из приватного ключа
    account = w3.eth.account.from_key(PRIVATE_KEY)
    deployer_address = account.address
    print("Deployer address:", deployer_address)

    # Компилируем контракт
    compiled_sol = compile_source(contract_source_code, solc_version="0.8.0")
    contract_id, contract_interface = compiled_sol.popitem()

    # Создаем контрактную фабрику
    SimpleStorage = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

    # Формируем транзакцию
    construct_txn = SimpleStorage.constructor().build_transaction({
        'from': deployer_address,
        'nonce': w3.eth.get_transaction_count(deployer_address),
        'gas': 3000000,
        'gasPrice': w3.to_wei('10', 'gwei')
    })

    # Подписываем транзакцию
    signed_txn = w3.eth.account.sign_transaction(construct_txn, private_key=PRIVATE_KEY)

    # Отправляем транзакцию
    tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
    print("Deploying contract, tx hash:", tx_hash.hex())

    # Ждем подтверждения
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Contract deployed at address:", tx_receipt.contractAddress)

if __name__ == "__main__":
    deploy_contract()
