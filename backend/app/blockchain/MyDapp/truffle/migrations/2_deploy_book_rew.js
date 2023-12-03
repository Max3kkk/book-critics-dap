const RewSystem  = artifacts.require("BookRewSystem");

module.exports = function (deployer) {
  deployer.deploy(RewSystem);
};
