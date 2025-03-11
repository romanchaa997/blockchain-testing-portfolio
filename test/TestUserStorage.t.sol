pragma solidity ^0.8.0;

import "forge-std/Test.sol";
import "../contracts/UserStorage.sol";

contract TestUserStorage is Test {
    UserStorage userStorage;

    function setUp() public {
        userStorage = new UserStorage();
    }

    function testSetAndGet() public {
        userStorage.set(777);
        assertEq(userStorage.get(address(this)), 777);
    }

    function testUnauthorizedGet() public {
        vm.expectRevert("Unauthorized access");
        vm.prank(address(0xBEEF));
        userStorage.get(address(this));
    }
}
