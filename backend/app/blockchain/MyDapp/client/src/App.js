import React, {useState, useEffect} from 'react';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import "./app.css";
import Web3 from 'web3';
import 'bootstrap/dist/css/bootstrap.min.css';
import BookCriticsPlatform from "./contracts/BookCriticsPlatform.json";
import BookTile from "./componentsFrontend/recipe-tile"; // Make sure this component is updated to handle the new book format
import BookDetail from './componentsFrontend/BookDetail'; // Import the BookDetail component

function App() {
    const [account, setAccount] = useState('');
    const [contract, setContract] = useState(null);
    const [books, setBooks] = useState([]); // Renamed from recipes to books for clarity

    const loadBlockchainData = async () => {
        const web3 = new Web3(Web3.givenProvider);
        const accounts = await web3.eth.getAccounts();
        setAccount(accounts[0]);

        const networkId = await web3.eth.net.getId();
        const deployedNetwork = BookCriticsPlatform.networks[networkId];
        const instance = new web3.eth.Contract(
            BookCriticsPlatform.abi,
            deployedNetwork && deployedNetwork.address,
        );

        setContract(instance);

        // Temporary mock data
        const mockBooks = [
            {
                index: 0,
                title: "Kitten Book",
                author: "John Doe",
                cover: "https://www.betterreading.com.au/wp-content/uploads/2020/02/shutterstock_165683546.png",
                votes: 123
            },
            {
                index: 1,
                title: "Book Book",
                author: "Jane Smith",
                cover: "https://i.pinimg.com/originals/23/bd/7f/23bd7f4e554fa6ad21a7fb0cb3f44bf0.jpg",
                votes: 456
            }
            // ... more books
        ];

        if (instance) {
            const result = await instance.methods.viewBooks().call();
            console.log(result);
            setBooks(mockBooks);
        }
    };

    useEffect(() => {
        loadBlockchainData();
    }, []);

    const HomePage = () => (
        <div className="app">
            <h1>Book Review Library</h1>
            <div className="app__books">
                {books.map(book => (
                    <BookTile book={book} key={book.index}/>
                ))}
            </div>
        </div>
    );

    return (
        <Router>
            <Routes>
                <Route exact path="/" element={<HomePage/>}/>
                <Route path="/book/:id" element={<BookDetail/>}/>
            </Routes>
        </Router>
    );
}

export default App;


