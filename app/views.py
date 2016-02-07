from flask import render_template, flash, redirect
from flask import jsonify
from app import app
from .forms import *
from .models import *

@app.route('/')
def index():
	return render_template('home.html', title='Home') 

@app.route('/api/members', methods=['GET'])
def get_members():
	members = []
	members = Member.query.all()
	response = [m.get_url() for m in members]
  	return jsonify({'response': response})

@app.route('/api/members/<int:id>', methods=['GET'])
def get_member(id):
	m = Member.query.get_or_404(id)
	return jsonify(m.to_json())

@app.route('/api/members/<int:id>/collections/', methods=['GET'])
def get_member_collections(id):
	m = Member.query.get_or_404(id)
	return jsonify({'response': [c.get_url() for c in m.collectiontransactions]})
	
@app.route('/api/collections', methods=['GET'])
def get_collections():
	collections = []
	response = []
	return jsonify({'response': response})

