from datetime import date

from pydantic import BaseModel


class Book(BaseModel):
    title: str
    summary: str
    publication_date: date
    author_id: int


class BookCreate(Book):
    pass


class Author(BaseModel):
    name: str
    bio: str


class AuthorCreate(Author):
    pass


class AuthorList(Author):
    id: int
    books: list[Book]

    class Config:
        orm_mode = True


class BookList(Book):
    id: int
    author: Author

    class Config:
        orm_mode = True
