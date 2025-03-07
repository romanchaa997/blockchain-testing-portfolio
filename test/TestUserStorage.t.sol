// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "forge-std/Test.sol";
import "../contracts/UserStorage.sol";

contract TestUserStorage is Test {
    UserStorage public userStorage;

    function setUp() public {
        userStorage = new UserStorage();
    }

    function testSelfSetAndGet() public {
        userStorage.set(123);
        assertEq(userStorage.get(), 123, "Stored value should be 123");
    }

    function testFailUnauthorizedGet() public {
        vm.prank(address(0x456));
        userStorage.get(); // Should fail
    }
}
