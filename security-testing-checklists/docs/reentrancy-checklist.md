# **Чек-лист по тестированию Reentrancy-атак в смарт-контрактах**

## **1. Введение**
### **Что такое Reentrancy?**
Reentrancy-атака – это уязвимость, при которой злоумышленник может повторно вызвать функцию контракта до завершения предыдущего вызова, что позволяет ему обойти проверки состояния и вывести больше средств, чем положено.

## **2. Ключевые проверки**
### **2.1. Анализ кода контракта**
- [ ] Проверить, есть ли вызовы `call`, `delegatecall`, `send`, `transfer`.
- [ ] Убедиться, что обновление состояния происходит **до** передачи ETH.
- [ ] Проверить, что контракт использует модификатор `reentrancyGuard` (из OpenZeppelin).
- [ ] Проверить, что баланс пользователя обновляется до выполнения внешнего вызова.

### **2.2. Автоматизированный анализ кода**
- [ ] Запустить **Slither** и проверить предупреждения (`slither . --check-reentrancy`).
- [ ] Использовать **Mythril** (`myth analyze <contract>`).
- [ ] Провести фаззинг с **Echidna** (`echidna-test config.yaml`).

### **2.3. Написание ручных тестов**
- [ ] Реализовать атаку через контракт-злоумышленник.
- [ ] Проверить, можно ли вывести средства несколько раз за один вызов.
- [ ] Проверить баланс контракта после атаки – он не должен уходить в ноль.
- [ ] Проверить работу защиты (если она есть): включение `reentrancyGuard`, обновление состояния перед вызовами.

## **3. Инструменты тестирования**
✅ **Slither** – статический анализатор кода.  
✅ **Mythril** – инструмент поиска уязвимостей.  
✅ **Echidna** – фаззинг-тестирование.  
✅ **Foundry** – быстрые тесты на Solidity.  
✅ **Web3.py + Pytest** – интеграционные тесты на Python.  

## **4. Пример уязвимого контракта**
```solidity
pragma solidity ^0.8.0;

contract Vulnerable {
    mapping(address => uint256) public balances;

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw() public {
        require(balances[msg.sender] > 0, "Insufficient balance");
        (bool success, ) = msg.sender.call{value: balances[msg.sender]}("");
        require(success, "Transfer failed");
        balances[msg.sender] = 0;  // <- Уязвимость! Состояние обновляется после перевода
    }
}
```

## **5. Пример тест-кейса на Web3.py**
```python
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
```

## **6. Улучшение защиты**
- [ ] Использовать `reentrancyGuard` из OpenZeppelin.
- [ ] Обновлять баланс **до** перевода средств (`balances[msg.sender] = 0;` перед `call`).
- [ ] Ограничить максимальное количество средств для вывода за один вызов.
- [ ] Использовать паттерн **Pull Payments** (раздельная логика хранения и передачи средств).

---
Этот чек-лист поможет обнаружить и протестировать Reentrancy-атаки, а также улучшить безопасность смарт-контрактов.
