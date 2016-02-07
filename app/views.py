from flask import render_template, flash, redirect
from flask import jsonify
from app import app
from .forms import *
from .models import *

@app.route('/')
def index():
	return render_template('home.html', title='Home') 

@app.route('/members', methods=['GET'])
def get_members():
	members = []
	members = Member.query.all()
  	return jsonify({'urls': members})

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
	m = Member.get_or_404(id)
	return jsonify(s.to_json())
	
@app.route('/collections', methods=['GET', 'POST'])
def collections():
	collections = []
	form = CollectionTransactionForm()
	form.member_id.choices = [h for h in Member.query.all()]

	if form.validate_on_submit():
		member_id = form.member_id.data
		or_number = form.or_number.data

  	return render_template('collections/collections.html', form=form, collections=collections, title='Collections') 
