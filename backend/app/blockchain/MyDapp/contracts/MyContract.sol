// contracts/MyContract.sol

pragma solidity ^0.8.21;

contract MyContract {
    uint private number;

    function setNumber(uint _number) public {
        number = _number;
    }

    function getNumber() public view returns (uint) {
        return number;
    }
}
