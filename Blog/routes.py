from Blog import app, db
from flask import render_template, redirect, url_for, request, jsonify
from Blog.models import Post
from flask_cors.decorator import cross_origin
from flask_expects_json import expects_json

schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 2,
                  "maxLength": 20},
        "body": {"type": "string", "minLength": 5,
                 "maxLength": 250},
        "author": {"type": "string", "minLength": 4,
                   "maxLength": 15}
    },
    "required": ["body", "title", "author"]
}


@app.route('/get', methods=["GET"])
@cross_origin()
def get_posts():
    posts = Post.query.all()
    return jsonify({"posts": [post.json_convert() for post in posts]})


# add to database
@app.route('/add', methods=["POST"])
@cross_origin()
# @expects_json(schema) //  to handle validation backend
def home_page():
    if request.method == 'POST':
        title = request.json['title']
        body = request.json['body']
        image = request.json['image']
        author = request.json['author']

        try:
            post = Post(title=title, body=body, image=image, author=author)
            db.session.add(post)
            db.session.commit()
            return jsonify({"post": post.json_convert()}), 201
        except AssertionError as exception_message:
            return "Aborted with 404", 404


@app.route('/get/<id>', methods=["GET"])
def get_one_post(id):
    post = Post.query.get(id)
    if post:
        return jsonify({"post": post.json_convert()}), 200
    else:
        return "Aborted with 404", 404


@app.route('/show', methods=["GET"])
def show():
    posts = Post.query.all()
    return render_template('show.html', posts=posts)


@app.route('/update/<id>', methods=["PUT"])
@cross_origin()
def update_post(id):
    post = Post.query.get(id)
    title = request.json['title']
    body = request.json['body']
    image = request.json['image']
    author = request.json['author']
    post.title = title
    post.body = body
    post.image = image
    post.author = author
    db.session.commit()
    return jsonify({"post": post.json_convert()}), 204


@app.route('/delete/<id>', methods=["DELETE"])
@cross_origin()
def delete_post(id):
    try:
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()
        return jsonify({"post": post.json_convert()}), 204
    except:
        return '404'
