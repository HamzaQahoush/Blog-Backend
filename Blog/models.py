from Blog import app, db
from datetime import datetime
from sqlalchemy.orm import validates


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String(length=1024), nullable=False)
    image = db.Column(db.String(), nullable=True)
    author = db.Column(db.String(length=30), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow(),onupdate=datetime.now)

    def __init__(self, title, body, image, author):
        self.title = title
        self.body = body
        self.image = image
        self.author = author

    def __repr__(self):
        return f'{self.title} {self.body}'

    def json_convert(self):
        return {"id": self.id, "title": self.title, "body": self.body, "image": self.image, "author": self.author,
                "date": self.date}

    # @validates('title')
    # def validate_title(self, key, title):
    #     if not title:
    #         raise AssertionError('No title provided')
    #     if len(title) < 5 or len(title) > 15:
    #         raise AssertionError('title must be between 5 and 15 characters')
    #     return title
    #
    # @validates('body')
    # def validate_body(self, key, body):
    #     if not body:
    #         raise AssertionError('No body provided')
    #     if len(body) < 5 or len(body) > 240:
    #         raise AssertionError('body must be between 5 and 250 characters')
    #     return body
    #
    # @validates('author')
    # def validate_author(self, key, author):
    #     if not author:
    #         raise AssertionError('No author provided')
    #     if len(author) < 5 or len(author) > 20:
    #         raise AssertionError('author must be between 4 and 15 characters')
    #     return author
