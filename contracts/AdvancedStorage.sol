// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AdvancedStorage {
    uint256[] private data;

    function add(uint256 _value) public {
        data.push(_value);
    }

    function remove(uint256 index) public {
        require(index < data.length, "Index out of bounds");
        // Видаляємо значення, замінюючи його останнім елементом
        data[index] = data[data.length - 1];
        data.pop();
    }

    function get(uint256 index) public view returns (uint256) {
        require(index < data.length, "Index out of bounds");
        return data[index];
    }

    function getAll() public view returns (uint256[] memory) {
        return data;
    }
}
