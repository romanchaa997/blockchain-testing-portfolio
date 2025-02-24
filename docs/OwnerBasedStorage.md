# OwnerBasedStorage Contract - Detailed Documentation

## Overview

This document provides a detailed description of the `OwnerBasedStorage` smart contract implemented in this project. The contract demonstrates an owner-based access control mechanism that ensures only the owner can update the stored data. Additionally, it emits an event upon a successful update, which is useful for off-chain monitoring and logging.

## Contract Description

**File:** `contracts/OwnerBasedStorage.sol`

**Purpose:**  
The `OwnerBasedStorage` contract is designed to store a single `uint256` value. It enforces an access control mechanism whereby only the contract owner (the account that deploys the contract) can update the stored value. Every time the value is updated via the `set()` function, an event `DataSet` is emitted, capturing the address of the updater and the new value.

**Key Features:**
- **Owner-Based Access Control:**  
  The contract assigns the deployer as the owner and restricts the `set()` function so that only the owner can call it.
- **Event Emission:**  
  When the stored data is updated, the contract emits a `DataSet` event with the details of the transaction.
- **Public Read Access:**  
  The `get()` function allows any user to retrieve the current stored value.

## Contract Code

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract OwnerBasedStorage {
    address public owner;
    uint256 private storedData;

    event DataSet(address indexed setter, uint256 value);

    constructor() {
        owner = msg.sender;
    }

    function set(uint256 _data) public {
        require(msg.sender == owner, "Only owner can set the data");
        storedData = _data;
        emit DataSet(msg.sender, _data);
    }

    function get() public view returns (uint256) {
        return storedData;
    }
}
