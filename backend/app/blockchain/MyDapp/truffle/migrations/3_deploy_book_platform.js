const BookCriticsToken = artifacts.require("BookCriticsToken");
const BookCriticsPlatform = artifacts.require("BookCriticsPlatform");

module.exports = async function (deployer) {
    await deployer.deploy(BookCriticsToken);
    const booktokenInstance = await BookCriticsToken.deployed();

    await deployer.deploy(BookCriticsPlatform, booktokenInstance.address);
};
