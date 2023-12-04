// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract BookReviewToken is ERC20 {
    address public owner;
    uint256 public rewardPerReview = 1 * (10 ** 18); // 1 Token per review

    struct Review {
        uint256 reviewId;
        address reviewer;
        uint256 rewardAmount;
    }

    Review[] public reviews;

    // Event declaration
    event ReviewRewarded(uint256 indexed reviewId, address indexed reviewer, uint256 rewardAmount);

    constructor() ERC20("BookReviewToken", "BRT") {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }

    function rewardForReview(uint256 reviewId, address reviewer) public onlyOwner {
        _mint(reviewer, rewardPerReview);
        reviews.push(Review(reviewId, reviewer, rewardPerReview));
        emit ReviewRewarded(reviewId, reviewer, rewardPerReview);
    }

    function getReviews() public view returns (Review[] memory) {
        return reviews;
    }

    // The following ERC20 methods are inherited from OpenZeppelin's ERC20 contract:
    // - function totalSupply() public view returns (uint256)
    // - function balanceOf(address account) public view returns (uint256)
    // - function transfer(address recipient, uint256 amount) public returns (bool)
    // - function allowance(address owner, address spender) public view returns (uint256)
    // - function approve(address spender, uint256 amount) public returns (bool)
    // - function transferFrom(address sender, address recipient, uint256 amount) public returns (bool)
    // - event Transfer(address indexed from, address indexed to, uint256 value)
    // - event Approval(address indexed owner, address indexed spender, uint256 value)
}
