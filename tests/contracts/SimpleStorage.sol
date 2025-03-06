// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 private storedData;

    // Устанавливаем значение
    function set(uint256 _data) public {
        storedData = _data;
    }

    // Получаем значение
    function get() public view returns (uint256) {
        return storedData;
    }
}
