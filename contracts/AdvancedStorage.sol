pragma solidity ^0.8.0;

contract AdvancedStorage {
    address public owner;
    uint[] private data;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    function add(uint _data) public onlyOwner {
        data.push(_data);
    }

    function get(uint index) public view returns (uint) {
        require(index < data.length, "Invalid index");
        return data[index];
    }
}
