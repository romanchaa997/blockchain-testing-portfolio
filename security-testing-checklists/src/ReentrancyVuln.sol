// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ReentrancyVuln {
    mapping(address => uint256) public balances;

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw() public {
        require(balances[msg.sender] > 0, "Insufficient balance");
        (bool success, ) = msg.sender.call{value: balances[msg.sender]}("");
        require(success, "Transfer failed");
        balances[msg.sender] = 0;  // Уязвимость! Обновление баланса после перевода
    }

    receive() external payable {}  // ✅ Позволяет контракту получать ETH
}
