// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract OwnerBasedStorage {
    address public owner;
    uint256 private storedData;

    event DataSet(address indexed setter, uint256 value);

    constructor() {
        owner = msg.sender;
    }

    function set(uint256 _data) public {
        // 🔥 ВАЖЛИВО: Впевнимося, що ця перевірка є у коді!
        require(msg.sender == owner, "Only owner can set the data");
        storedData = _data;
        emit DataSet(msg.sender, _data);
    }

    function get() public view returns (uint256) {
        return storedData;
    }
}
