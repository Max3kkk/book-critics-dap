import React, {useState, useEffect} from 'react';
import {useParams} from 'react-router-dom';
import BookTile from './recipe-tile'; // Adjust the path as needed

function BookDetail() {
    const [book, setBook] = useState(null);
    const [likes, setLikes] = useState(0);
    const {id} = useParams(); // Get the book ID from the URL

    const sampleReviews = [
        {id: 1, name: "Alice", date: "2021-01-01", text: "Great book!"},
        {id: 2, name: "Bob", date: "2021-02-15", text: "Very informative."},
        // Add more sample reviews here
    ];

    useEffect(() => {
        // Fetch the book data based on the ID
        // This is a mock function, replace with your actual data fetching logic
        const fetchBook = async () => {
            const fetchedBook = {
                index: 0,
                title: "Kitten Book",
                author: "John Doe",
                cover: "https://www.betterreading.com.au/wp-content/uploads/2020/02/shutterstock_165683546.png",
                votes: 123
            };
            setBook(fetchedBook);
        };

        fetchBook();
    }, [id]);

    const handleLike = () => {
        setLikes(likes + 1);
    };

    if (!book) {
        return <div>Loading book details...</div>;
    }

    return (
        <div className="book-detail">
            <BookTile book={book} key={book.index}/>
            <button onClick={handleLike}>Like</button>
            <span>{likes}</span>

            <div className="reviews">
                <h3>Reviews</h3>
                {sampleReviews.map((review) => (
                    <div key={review.id}>
                        <h4>{review.name}</h4>
                        <p>{review.date}</p>
                        <p>{review.text}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default BookDetail;
