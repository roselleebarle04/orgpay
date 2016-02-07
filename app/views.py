from flask import render_template, flash, redirect
from app import app
from .forms import *
from .models import *

@app.route('/')
def index():
	user = {'nickname': 'Miguel'}
	return render_template('home.html', title='Home', user=user) 

@app.route('/members')
def members():
	members = []
	results_count = 0
	try:
		members = Member.query.all()
		results_count = len(members)
	except:
		pass
  	return render_template('members/members.html', title='Members', members=members, results_count=results_count) 

@app.route('/collections', methods=['GET', 'POST'])
def collections():
	collections = []
	form = CollectionTransactionForm()
	form.member_id.choices = [h for h in Member.query.all()]

	if form.validate_on_submit():
		member_id = form.member_id.data
		or_number = form.or_number.data

  	return render_template('collections/collections.html', form=form, collections=collections, title='Collections') 

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404