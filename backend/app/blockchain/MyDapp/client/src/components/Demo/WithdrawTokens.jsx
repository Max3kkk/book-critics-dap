import React from 'react';

const WithdrawTokens = ({ account, contract }) => {
    const handleWithdraw = async () => {
        await contract.methods.withdrawTokens().send({ from: account });
    };

    return (
        <div>
            <button onClick={handleWithdraw}>Withdraw Tokens</button>
        </div>
    );
};

export default WithdrawTokens;
