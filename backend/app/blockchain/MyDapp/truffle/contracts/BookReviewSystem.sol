// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

// A simplified ERC20 token interface
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract BookReviewSystem {
    IERC20 public token;
    address public owner;
    uint256 public rewardAmount;
    uint256 public doublingPeriod; // in seconds
    uint256 public numberOfReviews;

    struct Review {
        uint256 timestamp;
        uint256 tokens;
	uint256 reviewIndex;
    }

    mapping(address => Review) public reviews;

    constructor(address tokenAddress, uint256 initialReward, uint256 _doublingPeriod) {
        token = IERC20(tokenAddress);
        owner = msg.sender;
        rewardAmount = initialReward;
        doublingPeriod = _doublingPeriod;
	numberOfReviews = 0;
    }

    // Ensure only the owner can call a function
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }

    // Update the reward amount
    function updateRewardAmount(uint256 newAmount) public onlyOwner {
        rewardAmount = newAmount;
    }

    // Submit a review
    function submitReview() public {
        reviews[msg.sender] = Review({
            timestamp: block.timestamp,
            tokens: rewardAmount,
	    reviewIndex: numberOfReviews
        });
	numberOfReviews = numberOfReviews + 1;

        // Transfer tokens to the contract for escrow
        require(token.transfer(address(this), rewardAmount), "Token transfer failed");
    }

    // Check the current token balance of a reviewer
    function checkBalance(address reviewer) public view returns (uint256) {
        if (reviews[reviewer].timestamp == 0) {
            return 0;
        }

        uint256 timeElapsed = block.timestamp - reviews[reviewer].timestamp;
        uint256 periodsElapsed = timeElapsed / doublingPeriod;
        return reviews[reviewer].tokens * (2 ** periodsElapsed);
    }

    // Withdraw tokens
    function withdrawTokens() public {
        uint256 balance = checkBalance(msg.sender);
        require(balance > 0, "No tokens to withdraw");

        // Reset the review
        delete reviews[msg.sender];

        // Transfer the tokens to the reviewer
        require(token.transfer(msg.sender, balance), "Token transfer failed");
    }
}
