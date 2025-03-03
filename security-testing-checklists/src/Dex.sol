// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Dex {
    mapping(address => uint256) public balances;

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Not enough balance");
        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
    }

    function swap(uint256 amount) public payable {
        require(msg.value == amount, "Incorrect ETH amount");
        balances[msg.sender] += amount;
    }
}
