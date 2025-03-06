# **Reentrancy Attack Testing Checklist for Smart Contracts**

## **1. Introduction**
### **What is Reentrancy?**
A reentrancy attack is a vulnerability where an attacker can call a contract function again before the previous call completes, allowing them to bypass state checks and withdraw more funds than intended.

## **2. Key Checks**
### **2.1. Contract Code Analysis**
- [ ] Check for `call`, `delegatecall`, `send`, `transfer` calls.
- [ ] Ensure that the state is updated **before** the ETH transfer.
- [ ] Ensure that the contract uses the `reentrancyGuard` modifier (from OpenZeppelin).
- [ ] Ensure that the user's balance is updated before the external call is made.

### **2.2. Automated code analysis**
- [ ] Run **Slither** and check for warnings (`slither . --check-reentrancy`).
- [ ] Use **Mythril** (`myth analyze <contract>`).
- [ ] Perform fuzzing with **Echidna** (`echidna-test config.yaml`).

### **2.3. Writing manual tests**
- [ ] Implement an attack through a malicious contract.
- [ ] Check if it is possible to withdraw funds multiple times in one call.
- [ ] Check the contract balance after the attack - it should not go to zero.
- [ ] Check the operation of protection (if any): enabling `reentrancyGuard`, updating the state before calls.

## **3. Testing tools**
✅ **Slither** is a static code analyzer.
✅ **Mythril** – vulnerability search tool.
✅ **Echidna** – fuzz testing.
✅ **Foundry** – fast tests on Solidity.
✅ **Web3.py + Pytest** – integration tests on Python.

## **4. Example of a vulnerable contract**
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

## **5. Example of a test case in Web3.py**
```python
import pytest
from web3 import Web3

def test_reentrancy_attack(w3, vulnerable_contract, attacker_contract):
# Deposit 1 ETH from the victim
tx = vulnerable_contract.functions.deposit().transact({'from': w3.eth.accounts[1], 'value': Web3.toWei(1, 'ether')})
w3.eth.wait_for_transaction_receipt(tx)

# Attack: call withdraw() via a malicious contract
tx = attacker_contract.functions.attack().transact({'from': w3.eth.accounts[2]})
w3.eth.wait_for_transaction_receipt(tx)

# Check the balance of the contract - it should be empty
assert w3.eth.get_balance(vulnerable_contract.address) == 0
```

## **6. Security Improvements**
- [ ] Use `reentrancyGuard` from OpenZeppelin.
- [ ] Update balance **before** funds transfer (`balances[msg.sender] = 0;` before `call`).
- [ ] Limit maximum amount of funds for withdrawal per call.
- [ ] Use **Pull Payments** pattern (separate logic for storing and transferring funds).

---
This checklist will help detect and test reentrancy attacks, as well as improve smart contract security.
