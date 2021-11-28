from Blog import app, db
from datetime import datetime


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String(length=1024), nullable=False)
    image = db.Column(db.String(), nullable=True)
    author = db.Column(db.String(length=30), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, title, body, image, author):
        self.title = title
        self.body = body
        self.image = image
        self.author = author

    def __repr__(self):
        return f'{self.title} {self.body}'

    def json_convert(self):
        return {"id": self.id, "title": self.title, "body": self.body, "image": self.image, "author": self.author}
# class PostSchema(ma.Schema):
# #     class meta:
# #         fields = ('id', 'title', 'body', 'image', 'author', 'date')
#

#
# post_schema = PostSchema(strict=True)  # for one article
# posts_schema = PostSchema(many=True)  # to query all the articles
