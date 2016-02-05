import unittest
from app import db, create_app
from app.models import * 
from app.utils import *

class AppTestCase(unittest.TestCase):

    def setUp(self):
    	self.app = create_app('testing')
    	self.app_context = self.app.app_context()
    	self.app_context.push()
    	db.create_all()

    def tearDown(self):
    	db.session.remove()
    	db.drop_all()
    	self.app_context.pop()

    def test_app_exists(self):
		self.assertFalse(current_app is None)
  #   def test_create_collection(self):
  #   	collection_data = {
		# 	'student_id': '2013-0038',
		# 	'or_number': 12701,
		# 	'date': 8/4/15,
		# 	'school_year': 2015-2016,
		# 	'term': 1,
		# 	'organization_fee_id': [1,2]
		# 	'total': 125,
		# }

if __name__ == '__main__':
    unittest.main()