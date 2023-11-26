from marshmallow import Schema, fields

class AuthorSchema(Schema):
  id = fields.Int(dump_only=True)
  name = fields.Str(required=True)

class BookSchema(Schema):
  id = fields.Int(dump_only=True)
  title = fields.Str(required=True)
  synopsis = fields.Str()

class AuthorWithBooksSchema(AuthorSchema):
  books = fields.List(fields.Nested(BookSchema()), dump_only=True)

class BookPathParamsSchema(Schema):
  author_id = fields.Int(required=True)

class BookWithAuthorSchema(BookSchema):
  author_name = fields.String(attribute='author.name', dump_only=True)