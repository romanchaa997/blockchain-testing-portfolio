// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

contract UserStorage {
    mapping(address => uint256) private userStorage;

    function set(uint _data) public {
        userStorage[msg.sender] = _data;
    }

    function get(address user) public view returns (uint) {
        require(msg.sender == user, "Unauthorized access");
        return userStorage[user];
    }
}
