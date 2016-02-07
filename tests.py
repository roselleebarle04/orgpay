import unittest
import json
from app import app
from app import db
from app.models import *

class AppTestCase(unittest.TestCase):

    def setUp(self):
        # self.app = create_app('testing')
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_new_collection(self):
        json_data = json.dumps(dict(member_id=1, or_number=12345))
        response = self.client.post('/api/collections/', content_type='application/json', data=json_data)
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()