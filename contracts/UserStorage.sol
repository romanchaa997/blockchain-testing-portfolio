// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract UserStorage {
    // Хранит значение для каждого пользователя
    mapping(address => uint256) private data;

    // Событие, генерируемое при обновлении значения
    event DataUpdated(address indexed user, uint256 newValue);

    // Функция для установки значения текущим пользователем
    function set(uint256 _data) public {
        data[msg.sender] = _data;
        emit DataUpdated(msg.sender, _data);
    }

    // Функция для получения значения, установленного текущим пользователем
    function get() public view returns (uint256) {
        return data[msg.sender];
    }

    // Функция для получения значения для заданного адреса
    function getFor(address _user) public view returns (uint256) {
        return data[_user];
    }
}
