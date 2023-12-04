import { EthProvider } from "./contexts/EthContext";
import Intro from "./components/Intro/";
import Setup from "./components/Setup";
import Demo from "./components/Demo";
import Footer from "./components/Footer";

import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import BookReviewToken from './contracts/BookReviewToken.json';
import SubmitReview from './components/Demo/SubmitReview';
import CheckBalance from './components/Demo/CheckBalance';
import WithdrawTokens from './components/Demo/WithdrawTokens';
import UpdateRewardAmount from './components/Demo/UpdateRewardAmount';

const App = () => {
  const [account, setAccount] = useState('');
  const [contract, setContract] = useState(null);

  useEffect(() => {
    const loadBlockchainData = async () => {
      const web3 = new Web3(Web3.givenProvider || "http://localhost:7545");
      const accounts = await web3.eth.getAccounts();
      setAccount(accounts[0]);

      const networkId = await web3.eth.net.getId();
      const deployedNetwork = BookReviewToken.networks[networkId];
      const instance = new web3.eth.Contract(
          BookReviewToken.abi,
        deployedNetwork && deployedNetwork.address,
      );

      setContract(instance);
    };

    loadBlockchainData();
  }, []);

  return (
    <div>
      <h1>Book Review System</h1>
	  {!contract ? (
        <p>Loading contract...</p>
      ) : (
        <>
          <p>Connected Account: {account}</p>
          <SubmitReview account={account} contract={contract} />
          <CheckBalance account={account} contract={contract} />
          <WithdrawTokens account={account} contract={contract} />
          <UpdateRewardAmount account={account} contract={contract} />
        </>
      )}
    </div>
  );
};

export default App;

