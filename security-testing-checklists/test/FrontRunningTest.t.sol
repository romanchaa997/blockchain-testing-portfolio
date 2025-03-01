// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "forge-std/Test.sol";
import "../contracts/Dex.sol";

contract FrontRunningTest is Test {
    Dex dex;
    address attacker = address(0xBEEF);
    address victim = address(0xCAFE);

    function setUp() public {
        dex = new Dex();
        vm.deal(attacker, 10 ether);
        vm.deal(victim, 10 ether);
    }

    function testFrontRunning() public {
        vm.prank(victim);
        dex.swap{value: 1 ether}(1 ether);

        vm.prank(attacker);
        vm.txGasPrice(2 gwei); // Атакующий отправляет транзакцию с повышенной комиссией
        dex.swap{value: 1 ether}(1 ether);

        assertTrue(tx.origin == attacker, "Front-running атака успешна");
    }
}
