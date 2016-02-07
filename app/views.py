from flask import render_template, flash, redirect, request
from flask import jsonify
from app import app
from app import db
from .forms import *
from .models import *

@app.route('/')
def index():
	return render_template('base.html', title='Home') 

@app.route('/api/members', methods=['GET'])
def get_members():
	members = Member.query.all()
	response = []
	for member in members:
		response.append(member.to_json())
  	return jsonify({'response': response})

@app.route('/api/members/<int:id>', methods=['GET'])
def get_member(id):
	m = Member.query.get_or_404(id)
	return jsonify(m.to_json())
	
@app.route('/api/collections', methods=['GET'])
def get_collections():
	collections = CollectionTransaction.query.all()
	response = [c.get_url() for c in collections]
	return jsonify({'response': response})

@app.route('/api/collections/<int:id>', methods=['GET'])
def get_collection(id):
	c = CollectionTransaction.query.get_or_404(id)
	return jsonify(c.to_json())

@app.route('/api/collections/', methods=['POST'])
def new_collection():
	n = CollectionTransaction()
	n.from_json(request.json)
	db.session.add(n)
	db.session.commit()
	response = jsonify({})
	response.status_code = 201
	response.headers['Location'] = n.get_url()
	return response

@app.route('/api/collections/<int:id>', methods=['PUT'])
def edit_collection(id):
	n = CollectionTransaction.query.get_or_404(id)
	n.from_json(request.json)
	db.session.add(n)
	db.sesion.commit()
	return jsonify({})

@app.route('/api/members/<int:id>/collections/', methods=['GET'])
def get_member_collections(id):
	m = Member.query.get_or_404(id)
	return jsonify({'response': [c.get_url() for c in m.collectiontransactions]})

def bad_request(message):
	response = jsonify({'error': 'bad request', 'message': message})

def not_found_error(e):
	response = jsonify({'error': 'Not Found', 'message': message})
	response.status_code = 404
	return response

@app.errorhandler(ValidationError)
def validation_error(e):
	return bad_request(e.args[0])

@app.errorhandler(404)
def not_found_error(e):
	print e
	return not_found_error(e.args[0])