import sqlalchemy
from db import Base
from sqlalchemy import orm


class Book(Base):
    __tablename__ = "Books"
    isbn = sqlalchemy.Column(sqlalchemy.String(100), nullable=False, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String(100), nullable=False)
    year_of_publishing = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    sqlalchemy.UniqueConstraint("title", "year_of_publishing",  name="books_un_1")
    