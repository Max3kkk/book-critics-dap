contract BookCriticsPlatform is Ownable {
    BookCriticsToken public token;

    struct Book {
        uint256 index;
        string title;
        string author;
        string cover;
        uint256 votes;
    }

    struct Review {
        address reviewer;
        string content;
    }

    Book[] public books;
    mapping(uint256 => Review[]) public bookReviews;
    mapping(address => uint256) public rewardsBalance;
    mapping(address => uint256) public lastUpdateTime;
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    uint256 public rewardPerReview = 10 * (10 ** 18);
    uint256 public rewardPerVote = 1 * (10 ** 18);
    uint256 public stakingRewardRate = 8; // Percentage rate per year

    constructor(address tokenAddress) Ownable(msg.sender) {
        token = BookCriticsToken(tokenAddress);
    }

    // Owner functions
    function addBook(string memory title, string memory author, string memory cover) public onlyOwner {
        books.push(Book(books.length, title, author, cover, 0));
    }

    function setRewards(uint256 reviewReward, uint256 voteReward) public onlyOwner {
        rewardPerReview = reviewReward;
        rewardPerVote = voteReward;
    }

    function setStakingRewardRate(uint256 rate) public onlyOwner {
        stakingRewardRate = rate;
    }

    // Internal function to update reward balance
    function _updateRewardBalance(address user) internal {
        if (lastUpdateTime[user] != 0) {
            uint256 timeElapsed = block.timestamp - lastUpdateTime[user];
            uint256 additionalReward = (rewardsBalance[user] * stakingRewardRate * timeElapsed) / (100 * 365 days);
            rewardsBalance[user] += additionalReward;
        }
        lastUpdateTime[user] = block.timestamp;
    }

    // User functions
    function leaveReview(uint256 bookId, string memory content) public {
        _updateRewardBalance(msg.sender);
        bookReviews[bookId].push(Review(msg.sender, content));
        rewardsBalance[msg.sender] += rewardPerReview;
    }

    function voteForBook(uint256 bookId) public {
        require(!hasVoted[bookId][msg.sender], "Already voted for this book");
        _updateRewardBalance(msg.sender);
        books[bookId].votes += 1;
        hasVoted[bookId][msg.sender] = true;
        rewardsBalance[msg.sender] += rewardPerVote;
    }

    function withdrawRewards(uint256 amount) public {
        _updateRewardBalance(msg.sender);
        require(amount <= rewardsBalance[msg.sender], "Insufficient balance");
        rewardsBalance[msg.sender] -= amount;
        token.mint(msg.sender, amount);
    }

    // View function to check updated reward balance
    function getUpdatedRewardBalance(address user) public view returns (uint256) {
        if (lastUpdateTime[user] == 0) return rewardsBalance[user];
        uint256 timeElapsed = block.timestamp - lastUpdateTime[user];
        uint256 additionalReward = (rewardsBalance[user] * stakingRewardRate * timeElapsed) / (100 * 365 days);
        return rewardsBalance[user] + additionalReward;
    }

    function viewBooks() public view returns (Book[] memory) {
        return books;
    }

    function viewBook(uint256 bookId) public view returns (Book memory) {
        return books[bookId];
    }

    function viewReviews(uint256 bookId) public view returns (Review[] memory) {
        return bookReviews[bookId];
    }
}
