// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract UserStorage {
    // Stores a value for each user
    mapping(address => uint256) private data;

    // Event generated when a value is updated
    event DataUpdated(address indexed user, uint256 newValue);

    // Function to set the value by the current user
    function set(uint256 _data) public {
        data[msg.sender] = _data;
        emit DataUpdated(msg.sender, _data);
    }

    // Function to get the value set by the current user
    function get() public view returns (uint256) {
        return data[msg.sender];
    }

    // Function to get the value for a given address
    function getFor(address _user) public view returns (uint256) {
        return data[_user];
    }
}
