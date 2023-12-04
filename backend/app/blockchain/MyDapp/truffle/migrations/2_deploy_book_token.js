const BookCriticsToken = artifacts.require("BookCriticsToken");

module.exports = function (deployer) {
    deployer.deploy(BookCriticsToken);
};
