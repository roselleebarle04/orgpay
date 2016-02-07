from flask import Flask, jsonify, make_response, abort, request
from flask_restful import Resource, Api
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
api = Api(app)

from app import views, models

# member_fields = {
# 	'student_id': fields.Integer, 
# 	'first_name': fields.String,
# 	'last_name': fields.String,
# 	'middle_initial': fields.String,
# 	'department_college': fields.String,
# 	'scholarship_description': fields.String,
# }

# collection_fields = {
# 	'member': member_fields,
# 	'or_number':  fields.Integer,
# }

# class Member(Resource):
# 	def get(self, id):
# 		s = Member.query.get(id)
# 		if not s:
# 			abort(404)
# 		return marshal(member_fields, s)
# api.add_resource(Member, '/api/v1/members/<int:id>')

# class Members(Resource):
# 	@marshal_with(member_fields)
# 	def post(self):
# 		args = parser.parse_args()
# 		s = Member(**args)

# 		db.session.add(s)
# 		db.commit()

# 		return s
# api.add_resource(Members, '/api/v1/members')
