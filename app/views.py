from flask import render_template, flash, redirect, request
from flask_restful import Resource, Api, reqparse, fields, marshal_with, marshal
from flask import jsonify
from app import app, api
from app import db
from .models import *


@app.route('/')
def index():
	return render_template('base.html', title='Home') 

@app.route('/api/members', methods=['GET'])
def get_members():
	""" Returns a json response containing a 'response' key that contains the array of 
	members formatted in a dictionary. 
	
	Returns 
	{
		'response': [
			{'name': 'member1', 'address': 'address2'},
			{'name': 'member1', 'address': 'address2'},
			....
		]
	}
	"""
	members = Member.query.all()
	response = []
	for member in members:
		response.append(member.to_json())
  	return jsonify({'response': response})

@app.route('/api/members/<int:id>', methods=['GET'])
def get_member(id):
	""" Returns a json response containing a 'response' key that contains an array containing the 
	member queries (in dict format) 
	
	Returns
	{
		'response': [
			{'name': 'member1', 'address': 'address1'}
		]
	}
	"""
	m = Member.query.get_or_404(id)
	return jsonify({'response': [m.to_json()]})

@app.route('/api/members/', methods=['POST'])
def new_member():
	m = Member()
	m.from_json(request.json)
	db.session.add(m)
	db.session.commit()
	response = jsonify({'response': [m.to_json()]})
	response.status_code = 201
	return response

@app.route('/api/members/<int:id>', methods=['PUT'])
def edit_member(id):
	n = Member.query.get_or_404(id)
	n.from_json(request.json)
	db.sesion.commit()
	return jsonify({'response': [n.to_json()]})

@app.route('/api/collections', methods=['GET'])
def get_collections():
	collections = CollectionTransaction.query.all()
	response = []
	for collection in collections:
		response.append(collection.to_json())
	return jsonify({'response': response})

@app.route('/api/collections/<int:id>', methods=['GET'])
def get_collection(id):
	c = CollectionTransaction.query.get_or_404(id)
	return jsonify({'response': [c.to_json()]})

@app.route('/api/collections/', methods=['POST'])
def new_collection():
	n = CollectionTransaction()
	n.from_json(request.json)
	db.session.add(n)
	db.session.commit()
	response = jsonify(n.to_json())
	response.status_code = 201
	return response

@app.route('/api/collections/<int:id>', methods=['PUT'])
def edit_collection(id):
	n = CollectionTransaction.query.get_or_404(id)
	n.from_json(request.json)
	db.sesion.commit()
	return jsonify({'collection': [n.to_json()]})

@app.route('/api/members/<int:id>/collections/', methods=['GET'])
def get_member_collections(id):
	m = Member.query.get_or_404(id)
	return jsonify({'response': [c.to_json() for c in m.collectiontransactions]})

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
	return not_found_error(e.args[0])