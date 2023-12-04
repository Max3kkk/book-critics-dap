const BookReviewToken = artifacts.require("BookReviewToken");

module.exports = function (deployer) {
    deployer.deploy(BookReviewToken);
};
