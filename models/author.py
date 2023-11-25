from db import db

class Author(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)

  books = db.relationship("Book", back_populates="author", lazy="dynamic")