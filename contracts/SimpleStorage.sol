// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

contract SimpleStorage {
    address public owner;
    uint private data;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    function set(uint _data) public onlyOwner {
        storedData = _data;
    }

    function get() public view returns (uint) {
        return storedData;
    }

    uint private storedData;
}
