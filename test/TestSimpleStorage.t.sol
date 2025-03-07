// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "forge-std/Test.sol";
import "../contracts/SimpleStorage.sol";

contract TestSimpleStorage is Test {
    SimpleStorage public simpleStorage;

    function setUp() public {
        simpleStorage = new SimpleStorage();
    }

    function testSetAndGet() public {
        simpleStorage.set(42);
        assertEq(simpleStorage.get(), 42, "Value should be 42");
    }

    function testFailUnauthorizedSet() public {
        vm.prank(address(0x123));
        simpleStorage.set(100); // Should fail
    }
}
