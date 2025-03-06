// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorageV2 {
    uint256 private storedData;

    // Функция set ограничивает значение максимум 1000
    function set(uint256 _data) public {
        require(_data <= 1000, "Value too high");
        storedData = _data;
    }

    function get() public view returns (uint256) {
        return storedData;
    }
}
