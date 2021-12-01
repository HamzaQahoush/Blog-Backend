from Blog import app, db
from Blog.models import Post
import unittest
import requests
import json
from flask import Flask, session


class ApiTest(unittest.TestCase):
    API_URL = 'http://127.0.0.1:5000/'
    get_posts_URL = f"{API_URL}get"
    post_obj = {
        "author": "hamzsa",
        "body": "This is body tested new test added",
        "date": "Wed, 01 Dec 2021 20:32:57 GMT",
        "id": 19,
        "image": "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg",
        "title": "Hello tested world "
    }
    updated_post = {
        "author": "Ali",
        "body": "This is body updated",
        "image": "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg",
        "title": "This updated"
    }

    updated_post_after = {
        "author": "Ali",
        "body": "This is body updated",
        "date": "Wed, 01 Dec 2021 20:32:57 GMT",
        "id": 19,
        "image": "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg",
        "title": "This updated"
    }
    invalid_add = {
        "author": "",
        "body": "This is body tested",
        "image": "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg",
        "title": ""
    }

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_all_post(self, ):
        r = requests.get(ApiTest.get_posts_URL)
        self.assertEqual(r.status_code, 200)

    def test_add_new_post(self):
        r = requests.post('http://127.0.0.1:5000/add', json=ApiTest.post_obj)
        self.assertEqual(r.status_code, 201)

    def test_get_added_post(self):
        # last_item = db.posts.query(Post).order_by(Post.id.desc()).first()
        # print(last_item, 'id')
        r = requests.get(f'{ApiTest.API_URL}get/{ApiTest.post_obj["id"]}')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['post'], ApiTest.post_obj)

    # def test_add_invalid_post(self):
    #     r = requests.post('http://127.0.0.1:4000/add', json=ApiTest.invalid_add)
    #
    #     self.assertEqual(r.status_code, 400)

    def test_update_existing_post(self):
        r = requests.put(f'{ApiTest.API_URL}update/{ApiTest.post_obj["id"]}', json=ApiTest.updated_post)
        self.assertEqual(r.status_code, 204)

    def test_get_post_after_updating(self):
        r = requests.get(f'{ApiTest.API_URL}get/{ApiTest.post_obj["id"]}')
        self.assertEqual(r.status_code, 200)
        self.assertDictEqual(r.json()['post'], ApiTest.updated_post_after)

    def test_delete_post(self):
        r = requests.delete(f'{ApiTest.API_URL}delete/{ApiTest.post_obj["id"]}')
        self.assertEqual(r.status_code, 204)

    def test_post_after_deletion(self):
        r = requests.get(f'{ApiTest.API_URL}get/{ApiTest.post_obj["id"]}')
        self.assertEqual(r.status_code, 404)


if __name__ == '__main__':
    unittest.main(verbosity=2)
