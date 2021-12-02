from Blog import app, db
from Blog.models import Post
import unittest
import requests


class ApiTest(unittest.TestCase):
    API_URL = 'http://127.0.0.1:5000/'
    get_posts_URL = f"{API_URL}get"
    post_obj = {
        "author": "hamzsa",
        "body": "This is body tested new test added",
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


    def test_get_all_post(self, ):
        r = requests.get(ApiTest.get_posts_URL)
        self.assertEqual(r.status_code, 200)

    def test_add_new_post(self):
        r = requests.post('http://127.0.0.1:5000/add', json=ApiTest.post_obj)
        self.assertEqual(r.status_code, 201)

    def test_get_added_post(self):
        last_item_id = db.session.query(Post).order_by(Post.id.desc()).first().id
        r = requests.get(f'{ApiTest.API_URL}get/{last_item_id}')
        self.assertEqual(r.status_code, 200)
        new_r = r.json()['post']
        del new_r['date']
        self.assertEqual(new_r, ApiTest.post_obj)

    @unittest.expectedFailure
    def test_add_invalid_post(self):
        r = requests.post('http://127.0.0.1:4000/add', json=ApiTest.invalid_add)

        self.assertEqual(r.status_code, 400)

    def test_update_existing_post(self):
        r = requests.put(f'{ApiTest.API_URL}update/{ApiTest.post_obj["id"]}', json=ApiTest.updated_post)
        self.assertEqual(r.status_code, 204)

    def test_get_post_after_updating(self):
        r = requests.get(f'{ApiTest.API_URL}get/{ApiTest.post_obj["id"]}')
        self.assertEqual(r.status_code, 200)
        new_r = r.json()['post']
        del new_r['date']
        self.assertDictEqual(new_r, ApiTest.updated_post_after)

    def test_delete_post(self):
        r = requests.delete(f'{ApiTest.API_URL}delete/{ApiTest.post_obj["id"]}')
        self.assertEqual(r.status_code, 204)

    def test_post_after_deletion(self):
        r = requests.get(f'{ApiTest.API_URL}get/{ApiTest.post_obj["id"]}')
        self.assertEqual(r.status_code, 404)


if __name__ == '__main__':
    unittest.main(verbosity=2)
