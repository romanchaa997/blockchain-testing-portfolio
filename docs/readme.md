Test Cases
    The following test cases have been implemented to verify the functionality
and security of the OwnerBasedStorage contract:

1. Deployment Test
  Objective: Verify that the contract is deployed correctly and that the owner is set to the deployer's address.
    Steps:
    1. Deploy the contract using w3.eth.default_account (i.e., accounts[0]).
    2. Check that owner equals w3.eth.accounts[0].
  Expected Result: The owner is correctly assigned.
2. Set Function Test (Owner)
  Objective: Verify that the owner can successfully update the stored data.
    Steps:
    1. Call set(123) from w3.eth.default_account.
    2. Verify that the get() function returns 123.
  Expected Result: The stored value is updated to 123.
3. Set Function Test (Non-Owner)
  Objective: Verify that non-owners are prevented from updating the stored data.
    Steps:
    1. Attempt to call set(999) from w3.eth.accounts[1].
    2. Expect the transaction to revert with the error message "Only owner can set the data".
  Expected Result: The transaction fails and the stored data remains unchanged.
4. Event Emission Test
  Objective: Ensure that the DataSet event is emitted with the correct parameters upon a successful call to set().
    Steps:
    1. Call set(777) from the owner.
    2. Retrieve the transaction receipt and parse the logs for the DataSet event.
    3. Verify that the event's setter is the owner's address and value is 777.
  Expected Result: A single DataSet event is emitted with the correct details.

    Conclusion
The OwnerBasedStorage contract implements essential smart contract patterns, such as owner-based access control and event emission for state changes. The comprehensive testing strategy includes positive tests, negative tests (preventing unauthorized access), and event verification, ensuring the contract behaves as expected in various scenarios.

This approach not only enhances the reliability of the contract but also demonstrates best practices in smart contract development and automated testing.