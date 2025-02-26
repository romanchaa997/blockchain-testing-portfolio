# Advanced Test Cases

This document describes the advanced test cases implemented in the project to ensure the quality and performance of the smart contracts.

## Test Cases

1. **Functional Test: Advanced Set/Get**
   - **Objective:** Verify that the `set()` function correctly updates the stored value and `get()` returns it.
   - **Steps:** Call `set(500)` and then call `get()`.
   - **Expected Result:** `get()` returns `500`.

2. **Negative Test: Invalid Value**
   - **Objective:** Verify that the contract reverts when an invalid value (greater than allowed limit) is set.
   - **Steps:** Attempt to call `set(1500)`.
   - **Expected Result:** Transaction is reverted with the error "Value too high".

3. **Load Test: Multiple Set Calls**
   - **Objective:** Measure the performance and stability when calling `set()` multiple times.
   - **Steps:** Call `set(i)` in a loop for 100 iterations.
   - **Expected Result:** The final value equals 99, and all transactions complete without error.

4. **Integration Test: Real Network Deployment**
   - **Objective:** Verify deployment of the contract on a real network (via Infura).
   - **Note:** This test is skipped if the account has insufficient funds.
  
5. **Integration Test: Infura Connectivity**
   - **Objective:** Ensure that the connection to Infura is successful and a valid block number is returned.
   - **Note:** This test is skipped if the account has insufficient funds.

## Checklist

- [ ] Functional tests pass and validate expected behaviors.
- [ ] Negative tests correctly revert invalid operations.
- [ ] Load tests complete within an acceptable time frame.
- [ ] Integration tests are marked as skipped when insufficient funds are available.
- [ ] Test reports and logs are properly generated and reviewed.

# Advanced Test Cases and Checklists

## Overview
The project includes a comprehensive suite of tests covering functional, negative, load, and integration scenarios for smart contracts on Ethereum. Some tests that require real network conditions (e.g., contract deployment via Infura) are marked as skipped if the required conditions (such as sufficient test ETH) are not met.

## Test Cases

1. **Functional Tests:**
   - **SimpleStorage Functional Test:**  
     Verify that `set()` correctly updates the value and `get()` returns the updated value.
   - **Event Emission Test:**  
     Ensure that calling `set()` emits the expected event with correct parameters.

2. **Negative Tests:**
   - **Invalid Input Test:**  
     Verify that the contract reverts the transaction when invalid data is provided.
   - **Unauthorized Access Test:**  
     For contracts with owner-based access control, confirm that functions revert when called by non-owner accounts.

3. **Load and Performance Tests:**
   - **High Load Simulation:**  
     Execute a loop of 1000 `set()` calls and measure total execution time and average gas usage.

4. **Integration and Deployment Tests:**
   - **Deployment Test:**  
     Automatically deploy the contract to the Sepolia network via Infura.
     *Note:* This test is marked as skipped if the account does not have sufficient funds.
     ```python
     @pytest.mark.skip(reason="Deployment test skipped due to insufficient funds")
     def test_deployment_real_network():
         ...
     ```
   - **Infura Connection Test:**  
     Verify connectivity to the Sepolia network through Infura and check that a valid block number is returned.

## Checklists
- [ ] Verify contract deployment and address assignment.
- [ ] Confirm functional correctness (set/get operations).
- [ ] Validate event emission upon state changes.
- [ ] Ensure negative test scenarios revert transactions as expected.
- [ ] Simulate load and record performance metrics.
- [ ] Check integration tests for network connectivity (Infura).
- [ ] Mark tests that depend on external funds with a skip decorator until conditions are met.
