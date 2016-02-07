from app import app
import urllib2
import unittest
import nose
from nose.tools import *

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_members(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_create_collection(self):
        # Create New
        rv, json = self.app.post('/api/collections/', data={'member_id': 1, 'or_number': '12345'})
        self.assertTrue(rv.status_code == 201)

if __name__ == '__main__':
    unittest.main()