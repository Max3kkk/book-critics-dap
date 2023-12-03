import React, { useState } from 'react';

const UpdateRewardAmount = ({ account, contract }) => {
    const [newAmount, setNewAmount] = useState('');

    const handleUpdate = async () => {
        await contract.methods.updateRewardAmount(newAmount).send({ from: account });
    };

    return (
        <div>
            <input type="number" value={newAmount} onChange={e => setNewAmount(e.target.value)} />
            <button onClick={handleUpdate}>Update Reward Amount</button>
        </div>
    );
};

export default UpdateRewardAmount;
