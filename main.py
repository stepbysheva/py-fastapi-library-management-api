from __future__ import annotations

from fastapi import FastAPI, Depends
from fastapi_pagination import add_pagination, paginate, Page

import schemas
from crud import list_all_books, create_book, list_all_authors, create_author, get_author
from database import SessionLocal

app = FastAPI()

add_pagination(app)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/books/", response_model=Page[schemas.BookList])
def list_all_books_end(db=Depends(get_db),
                       author_id: int | None = None):
    return paginate(list_all_books(db, author_id))


@app.post("/books/", response_model=schemas.Book)
def list_all_books_end(book: schemas.BookCreate, db=Depends(get_db)):
    return create_book(db, book)


@app.get("/authors/", response_model=Page[schemas.AuthorList])
def list_authors_end(db=Depends(get_db)):
    return paginate(list_all_authors(db))


@app.post("/authors/", response_model=schemas.Author)
def create_new_author(author: schemas.AuthorCreate, db=Depends(get_db)):
    return create_author(db, author)


@app.get("/authors/{id}/", response_model=schemas.Author)
def get_single_author(id,  db=Depends(get_db)):
    return get_author(db, id)
