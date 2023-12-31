from db import db

class Author(db.Model):
  __tablename__ = "authors"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)

  books = db.relationship("Book", back_populates="author", lazy="dynamic", cascade="all, delete")