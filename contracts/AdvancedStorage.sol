// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AdvancedStorage {
    uint256 private storedData;

    event DataSet(address indexed setter, uint256 value);

    // Set value function with limit
    function set(uint256 _data) public {
        require(_data <= 1000, "Value too high");
        storedData = _data;
        emit DataSet(msg.sender, _data);
    }

    // Function to get the value
    function get() public view returns (uint256) {
        return storedData;
    }
}
