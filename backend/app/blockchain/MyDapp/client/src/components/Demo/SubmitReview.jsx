import React, { useState, useEffect } from 'react';
import BookReviewToken from '../../contracts/BookReviewToken.json';
import Web3 from 'web3';

const SubmitReview = ({ account }) => {
    const [web3, setWeb3] = useState(new Web3(Web3.givenProvider || "http://localhost:7545"));
    const [contract, setContract] = useState(null);

    // Initialize contract
    useEffect(() => {
        const initContract = async () => {
            const networkId = await web3.eth.net.getId();
            const deployedNetwork = BookReviewToken.networks[networkId];
            const instance = new web3.eth.Contract(
                BookReviewToken.abi,
                deployedNetwork && deployedNetwork.address,
            );
            setContract(instance);
        };
        initContract();
    }, []);

    // Function to submit a review
    const handleSubmitReview = async () => {
        await contract.methods.rewardForReview(0, account).send({ from: account });
    };

    return (
        <div>
            <button onClick={handleSubmitReview}>Submit Review</button>
        </div>
    );
};

export default SubmitReview;
