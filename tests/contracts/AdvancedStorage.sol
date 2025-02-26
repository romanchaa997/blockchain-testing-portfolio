// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AdvancedStorage {
    uint256 private storedData;

    event DataSet(address indexed setter, uint256 value);

    // Функция установки значения с ограничением
    function set(uint256 _data) public {
        require(_data <= 1000, "Value too high");
        storedData = _data;
        emit DataSet(msg.sender, _data);
    }

    // Функция получения значения
    function get() public view returns (uint256) {
        return storedData;
    }
}
