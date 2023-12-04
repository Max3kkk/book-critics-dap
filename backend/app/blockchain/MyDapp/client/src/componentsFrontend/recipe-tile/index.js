import React from "react";
import "./style.css";
import { useNavigate } from "react-router-dom";

export default function BookTile({ book }) {
    const navigate = useNavigate();

    const handleTileClick = () => {
        navigate(`/book/${book.index}`); // Navigates to the detail page of the book
    };

    return (
        book.cover.match(/\.(jpeg|jpg|gif|png)$/) != null && (
            <div className="recipeTile" onClick={handleTileClick}>
                <img className="recipeTile__img" src={book.cover} alt={book.title} />
                <p className="recipeTile__name">{book.title}</p>
                <p className="recipeTile__author">{book.author}</p>
                <p className="recipeTile__votes">Votes: {book.votes}</p>
            </div>
        )
    );
}
