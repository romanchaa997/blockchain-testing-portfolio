// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

import "forge-std/Test.sol";
import "../contracts/SimpleStorage.sol";

contract TestSimpleStorage is Test {
    SimpleStorage simpleStorage;

    function setUp() public {
        simpleStorage = new SimpleStorage();
    }

    function testSetAndGet() public {
        simpleStorage.set(123);
        assertEq(simpleStorage.get(), 123);
    }

    function testUnauthorizedSet() public {
        vm.expectRevert("Only owner can call this function");
        vm.prank(address(0xBEEF));
        simpleStorage.set(999);
    }
}
