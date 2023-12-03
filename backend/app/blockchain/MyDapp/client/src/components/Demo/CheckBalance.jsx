import React, { useState, useEffect } from 'react';

const CheckBalance = ({ account, contract }) => {
    const [balance, setBalance] = useState(0);

    useEffect(() => {
        const getBalance = async () => {
            const result = await contract.methods.checkBalance(account).call();
            setBalance(result);
        };
        getBalance();
    }, [account, contract]);

    return (
        <div>
            Your Balance: {balance}
        </div>
    );
};
