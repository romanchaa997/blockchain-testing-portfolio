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
