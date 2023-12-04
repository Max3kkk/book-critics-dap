const MetaCoin = artifacts.require("MetaCoin");
const BookReviewSystem = artifacts.require("BookReviewSystem");

module.exports = async function (deployer) {
    await deployer.deploy(MetaCoin);
    const metaCoinInstance = await MetaCoin.deployed();

    // Replace these values with the appropriate values for your scenario
    const initialReward = 100; // Initial reward amount
    const doublingPeriod = 3600; // Doubling period in seconds (e.g., 1 hour)

    await deployer.deploy(BookReviewSystem, metaCoinInstance.address, initialReward, doublingPeriod);
};
