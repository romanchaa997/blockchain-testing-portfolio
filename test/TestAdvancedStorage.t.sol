// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "forge-std/Test.sol";
import "../contracts/AdvancedStorage.sol";

contract TestAdvancedStorage is Test {
    AdvancedStorage public advancedStorage;

    function setUp() public {
        advancedStorage = new AdvancedStorage();
    }

    function testAddAndRetrieve() public {
        advancedStorage.add(10);
        advancedStorage.add(20);

        uint256[] memory values = advancedStorage.getAll();
        assertEq(values.length, 2, "Should have two values stored");
        assertEq(values[0], 10, "First value should be 10");
        assertEq(values[1], 20, "Second value should be 20");
    }

    function testFailRemoveOutOfBounds() public {
        advancedStorage.remove(0); // Should fail as array is empty
    }
}
