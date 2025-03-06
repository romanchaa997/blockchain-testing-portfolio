Goal: Verify that the SimpleStorage contract is deployed successfully and receives a valid address.
Steps:

Deploy the contract to a local network (Ganache).
Verify that the get() method returns an initial value (e.g. 0).
Expected result: The contract has a valid address and the initial value is 0.
Functional test for set() and get() in SimpleStorage
Goal: Verify that the set() function correctly updates the value, and get() returns the updated value.
Steps:

Call the set(42) function.
Call the get() function.
Expected result: get() returns the value 42.
Negative test for SimpleStorageV2 (value constraint)
Goal: Verify that the set() function in the modified contract rolls back the transaction when an invalid value is passed (e.g. > 1000).
Steps:

Call set(2000) from another account or in the contract where the limit is set.
Expected result: The transaction is rolled back with the message "Value too high".
SimpleStorage boundary value test
Goal: Check that the contract correctly handles the maximum possible value for the uint256 type.
Steps:

Call set(2**256 - 1).
Verify that get() returns this value.
Expected result: The value is successfully set and returned.
SimpleStorage event emission test
Goal: Check that calling set() generates an event with the correct parameters.
Steps:

Call set(77) and get a transaction receipt.
Parse the logs for the event (e.g. DataSet).
Expected result: An event with the specified value and sender address is emitted.
Deployment Test for OwnerBasedStorage
Goal: Verify that the OwnerBasedStorage contract correctly sets the owner when deployed.
Steps:

Deploy the contract using the accounts[0] account.
Verify that the owner() function returns accounts[0].
Expected Result: The owner is the account used for the deployment.
Negative Test for the set() Function in OwnerBasedStorage
Goal: Verify that the set() function rolls back the transaction if called from a non-owner.
Steps:

Attempt to call set(999) from the accounts[1] account.
Expected Result: The transaction rolls back with the error "Only owner can set the data".
Separate Storage Test in UserStorage
Goal: Verify that different users can independently persist their values.
Steps:

User accounts[0] sets the value to 100.
User accounts[1] sets the value to 200.
Use getFor() to check that accounts[0] returns 100 and accounts[1] returns 200.
Expected result: The values ​​are stored independently for each user.
Integration test for connection via Infura (Sepolia)
Goal: Check that the application can connect to the public test network via Infura.
Steps:

Use the Infura URL for the Sepolia network.
Verify that the w3.is_connected() call returns True and the current block number can be retrieved.
Expected result: Successful connection, block number > 0.
Load testing
Goal: Evaluate the performance of the contract when executing a large number of transactions.
Steps:

Run 1000 calls to set() (or similar) in a loop.
Measure the total execution time and average gas consumption.
Expected Result: All transactions are completed in a reasonable time, without errors.