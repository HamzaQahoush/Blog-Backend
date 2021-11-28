from Blog import app, db
from flask import render_template, redirect, url_for, request, jsonify
from Blog.models import Post
from flask_cors.decorator import cross_origin


@app.route('/get', methods=["GET"])
@cross_origin()
def get_posts():
    posts = Post.query.all()
    return jsonify({"posts": [post.json_convert() for post in posts]})


@app.route('/', methods=["POST"])
@cross_origin()
def home_page():
    if request.method == 'POST':
        title = request.json['title']
        body = request.json['body']
        image = request.json['image']
        author = request.json['author']
        post = Post(title=title, body=body, image=image, author=author)
        db.session.add(post)
        db.session.commit()
        return jsonify({"post": post.json_convert()})


@app.route('/show', methods=["GET"])
def show():
    posts = Post.query.all()
    return render_template('show.html', posts=posts)


@app.route('/update/<id>/', methods=["PUT"])
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
    return jsonify({"post": post.json_convert()})


@app.route('/delete/<id>/', methods=["DELETE"])
def delete_post(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({"post": post.json_convert()})


