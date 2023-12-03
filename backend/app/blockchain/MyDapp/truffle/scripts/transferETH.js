const Web3 = require('web3');

module.exports = async function(callback) {
    try {
        // Initialize web3
        const web3 = new Web3(Web3.givenProvider || "http://localhost:8545");

        // List accounts
        const accounts = await web3.eth.getAccounts();

        // Specify the sender and receiver
        const sender = accounts[1]; // first account in the list
        //const receiver = '0x41c40EAa13cb8CF15a50EFD8157D673B7238d729'; // second account in the list
	const receiver = '0x7D7B71305c83fAeF856Ff12C1C3aC27f278074c9';
	const amount = web3.utils.toWei('20', 'ether'); // amount to send (1 ETH)

        // Transfer ETH
        const receipt = await web3.eth.sendTransaction({from: sender, to: receiver, value: amount});
        console.log('Transaction successful. Receipt:', receipt);
    } catch (error) {
        console.error('An error occurred:', error);
    }

    callback();
};
