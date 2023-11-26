from db import db

class Book(db.Model):
  __tablename__ = "books"

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), unique=False, nullable=False)
  synopsis = db.Column(db.String(4000), nullable=True)
  author_id = db.Column(db.Integer, db.ForeignKey("authors.id"), unique=False, nullable=False)

  author = db.relationship("Author", back_populates="books")