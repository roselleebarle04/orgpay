from flask import Flask, jsonify, make_response, abort, request

app = Flask(__name__)

tasks = [
	{
		'id': 1, 
		'title': u'Buy groceries',
		'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
		'done': False, 
	},
	{
		'id': 2, 
		'title': u'Learn Python',
		'description': u'Need to find it',
		'done': False
	}
]

@app.route('/orgpay/api/v1.0/tasks', methods=['GET'])
def get_tasks():
	return jsonify({'tasks': tasks})

@app.route('/orgpay/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
	task = filter(lambda t: t['id'] == task_id, tasks)
	if len(task) == 0:
		abort(404)
	return jsonify({'task': task[0]})

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not Found'}), 404)

@app.route('/orgpay/api/v1.0/tasks', methods=['POST'])
def create_task():
	if not request.json or not 'title' in request.json:
		abort(404)
	
	task = {
		'id': tasks[-1]['id'] + 1,
		'title': request.json['title'],
		'description': request.json.get('description', ""),
		'done': False
	}
	tasks.append(task)

	return jsonify({'task': task}), 201

@app.route('/orgpay/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
	task = filter(lambda t: t['id'] == task_id, tasks)
	if len(task) == 0:
		abort(404)
	if not request.json:
		abort(404)
	if 'title' in request.json and type(request.json['title']) != unicode:
		abort(404)
	if 'description' in request.json and type(request.json['description']) is not unicode:
		abort(400)
	if 'done' in request.json and type(request.json['done']) is not bool :
		abort(400)

	task[0]['title'] = request.json.get('title', task[0]['title'])
	task[0]['description'] = request.json.get('description', task[0]['description'])
	task[0]['done'] = request.json.get('done', task[0]['done'])
	return jsonify({'task': task[0]})

@app.route('/orgpay/api/v1.0/tasks/<int:task_id>', methods = ['DELETE'])
def delete_task(task_id):
	task = filter( lambda t: t['id'] == task_id, tasks)
	if len(task) == 0:
		abort(404)
	tasks.remove(task[0])
	return jsonify( { 'result': True } )

if __name__ == '__main__':
	app.run(debug=True)



