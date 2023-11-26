from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import *
from schemas import AuthorSchema, AuthorWithBooksSchema

blp = Blueprint("Authors", __name__)

@blp.get("/authors")
@blp.response(200, AuthorSchema(many=True))
def index():
  return Author.query.all()

@blp.get("/authors/<int:author_id>")
@blp.response(200, AuthorWithBooksSchema)
def show(author_id):
  author = Author.query.get_or_404(author_id)
  return author

@blp.post("/authors")
@blp.arguments(AuthorSchema)
@blp.response(201, AuthorSchema)
def create(author_data):
  author = Author(**author_data)
  try:
    db.session.add(author)
    db.session.commit()
  except SQLAlchemyError:
    abort(500, message="Um erro inesperado ocorreu")
  
  return author