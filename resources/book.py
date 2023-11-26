from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import *
from schemas import BookSchema, BookWithAuthorSchema, BookPathParamsSchema

blp = Blueprint("Books", __name__)

@blp.get("/books")
@blp.response(200, BookWithAuthorSchema(many=True))
def index():
  return Book.query.all()

@blp.get("/books/<int:book_id>")
@blp.response(200, BookWithAuthorSchema)
def show(book_id):
  book = Book.query.get_or_404(book_id)

  return book

@blp.delete("/books/<int:book_id>")
def delete(book_id):
  book = Book.query.get_or_404(book_id)
  try:
    db.session.delete(book)
    db.session.commit()
  except SQLAlchemyError:
    abort(500, message="Um erro inesperado ocorreu")

  return { "message": "Livro excluído" }, 200

@blp.get("/authors/<int:author_id>/books")
@blp.response(200, BookSchema(many=True))
def show_authors_books(author_id):
  books = Book.query.filter(Book.author_id == author_id).all()

  return books

@blp.post("/authors/<int:author_id>/books")
@blp.arguments(BookPathParamsSchema, location="path")
@blp.arguments(BookSchema)
@blp.response(201, BookWithAuthorSchema)
def create(path_params, book_data, author_id):
  author = Author.query.get(author_id)
  if not author:
    abort(404, message="Autor não existente")
  
  book = Book(**book_data, author_id=author.id)
  try:
    db.session.add(book)
    db.session.commit()
  except SQLAlchemyError:
    abort(500, message="Um erro inesperado ocorreu")
  
  return book