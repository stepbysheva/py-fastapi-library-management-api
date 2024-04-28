from sqlalchemy.orm import Session

from models import DBBook, DBAuthor


def list_all_books(db: Session, author_id):
    queryset = db.query(DBBook).all()
    if author_id:
        queryset.filter(DBBook.author_id == author_id)
    return queryset


def create_book(db: Session, book):
    new_book = DBBook(title=book.title,
                      summary=book.summary,
                      publication_date=book.publication_date,
                      author_id=book.author_id)

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book


def list_all_authors(db: Session):
    return db.query(DBAuthor).all()


def create_author(db: Session, author):
    new_author = DBAuthor(name=author.name, bio=author.bio)

    db.add(new_author)
    db.commit()
    db.refresh(new_author)

    return new_author


def get_author(db: Session, id):
    return db.query(DBAuthor).filter(DBAuthor.id == id).first()
