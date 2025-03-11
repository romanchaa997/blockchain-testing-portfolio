pragma solidity ^0.8.28;

import "forge-std/Test.sol";
import "../contracts/AdvancedStorage.sol";

contract TestAdvancedStorage is Test {
    AdvancedStorage advancedStorage;

    function setUp() public {
        advancedStorage = new AdvancedStorage();
    }

    function testAddAndRetrieve() public {
        advancedStorage.add(123);
        advancedStorage.add(456);

        assertEq(advancedStorage.get(0), 123);
        assertEq(advancedStorage.get(1), 456);
    }

    function testUnauthorizedSet() public {
        vm.prank(address(0xBEEF));
        vm.expectRevert("Only owner can call this function");
        advancedStorage.add(999);
    }
}
