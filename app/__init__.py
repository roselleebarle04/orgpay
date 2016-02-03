from flask import Flask, jsonify, make_response, abort, request
from flask.ext.restful import Api, Resource, reqparse, fields, marshal, marshal_with
from flask.ext.sqlalchemy import SQLAlchemy


member_fields = {
	'student_id': fields.Integer, 
	'first_name': fields.String,
	'last_name': fields.String,
	'middle_initial': fields.String,
	'department_college': fields.String,
	'scholarship_description': fields.String,
}

collection_fields = {
	'member': member_fields,
	'or_number':  fields.Integer,
}

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)

from app import views

# app.config.from_object('config')
# app.config.from_pyfile('config.py')

# db = SQLAlchemy(app)

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



# class MemberListAPI(Resource):
#     def get(self):
#         pass

#     def post(self):
#         pass

# class MemberAPI(Resource):
#     def get(self, id):
#         pass

#     def put(self, id):
#         pass

#     def delete(self, id):
#         pass

# api.add_resource(TaskListAPI, '/api/v1/members', endpoint = 'members')
# api.add_resource(TaskAPI, '/api/v1/members/<int:id>', endpoint = 'member')


# task_fields = {
#     'title': fields.String,
#     'description': fields.String,
#     'done': fields.Boolean,
#     'uri': fields.Url('task')
# }

# @app.route('/api/v1/tasks', methods=['GET'])
# def get_tasks():
# 	return jsonify({'tasks': tasks})

# @app.route('/api/v1/tasks/<int:task_id>', methods=['GET'])
# def get_task(task_id):
# 	task = filter(lambda t: t['id'] == task_id, tasks)
# 	if len(task) == 0:
# 		abort(404)
# 	return jsonify({'task': task[0]})

# @app.errorhandler(404)
# def not_found(error):
# 	return make_response(jsonify({'error': 'Not Found'}), 404)

# @app.route('/api/v1/tasks', methods=['POST'])
# def create_task():
# 	if not request.json or not 'title' in request.json:
# 		abort(404)
	
# 	task = {
# 		'id': tasks[-1]['id'] + 1,
# 		'title': request.json['title'],
# 		'description': request.json.get('description', ""),
# 		'done': False
# 	}
# 	tasks.append(task)

# 	return jsonify({'task': task}), 201

# @app.route('/api/v1/tasks/<int:task_id>', methods=['PUT'])
# def update_task(task_id):
# 	task = filter(lambda t: t['id'] == task_id, tasks)
# 	if len(task) == 0:
# 		abort(404)
# 	if not request.json:
# 		abort(404)
# 	if 'title' in request.json and type(request.json['title']) != unicode:
# 		abort(404)
# 	if 'description' in request.json and type(request.json['description']) is not unicode:
# 		abort(400)
# 	if 'done' in request.json and type(request.json['done']) is not bool :
# 		abort(400)

# 	task[0]['title'] = request.json.get('title', task[0]['title'])
# 	task[0]['description'] = request.json.get('description', task[0]['description'])
# 	task[0]['done'] = request.json.get('done', task[0]['done'])
# 	return jsonify({'task': task[0]})

# @app.route('/api/v1/tasks/<int:task_id>', methods = ['DELETE'])
# def delete_task(task_id):
# 	task = filter( lambda t: t['id'] == task_id, tasks)
# 	if len(task) == 0:
# 		abort(404)
# 	tasks.remove(task[0])
# 	return jsonify( { 'result': True } )

if __name__ == '__main__':
	app.run(debug=True)



