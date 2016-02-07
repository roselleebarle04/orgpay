import unittest
import json
import os
import app
import tempfile 
from app import db
from app.models import *

TEST_DB = 'test.db'

class AppTestCase(unittest.TestCase):

    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.app.config['TESTING'] = True
        app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, TEST_DB)
        self.app = app.app.test_client()
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_create_new_collection(self):
        json_data = json.dumps(dict(member_id=1, or_number=12345))
        response = self.app.post('/api/collections/', content_type='application/json', data=json_data)
        self.assertEqual(response.status_code, 201)



if __name__ == '__main__':
    unittest.main()