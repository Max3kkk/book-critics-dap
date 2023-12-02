import typing as t

from fastapi import APIRouter, Depends, Response

from app.db.crud.author_crud import (
    get_authors,
    create_author,
    edit_author,
    delete_author,
    get_author,
)
from app.db.schemas.author_schemas import Author, AuthorCreate
from app.db.session import get_db

author_router = r = APIRouter()


@r.get(
    "",
    response_model=t.List[Author],
    response_model_exclude_none=True,
)
async def authors_list(
    response: Response,
    db=Depends(get_db),
):
    """
    Get all authors
    """
    authors = get_authors(db)
    response.headers["Content-Range"] = f"0-9/{len(authors)}"
    return authors


@r.get(
    "/{author_id}",
    response_model=Author,
    response_model_exclude_none=True,
)
async def author_details(
    author_id: int,
    db=Depends(get_db),
):
    """
    Get any author details
    """
    author = get_author(db, author_id)
    return author
    # return encoders.jsonable_encoder(
    #     author, skip_defaults=True, exclude_none=True,
    # )


@r.post("", response_model=Author, response_model_exclude_none=True)
async def author_create(
    author: AuthorCreate,
    db=Depends(get_db),
):
    """
    Create a new author
    """
    return create_author(db, author)


@r.put("/{author_id}", response_model=Author, response_model_exclude_none=True)
async def author_edit(
    author_id: int,
    author: AuthorCreate,
    db=Depends(get_db),
):
    """
    Update existing author
    """
    return edit_author(db, author_id, author)


@r.delete("/{author_id}", response_model=Author, response_model_exclude_none=True)
async def author_delete(
    author_id: int,
    db=Depends(get_db),
):
    """
    Delete existing author
    """
    return delete_author(db, author_id)
