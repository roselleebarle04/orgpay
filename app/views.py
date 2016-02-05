from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from .models import *

@app.route('/')
def index():
	user = {'nickname': 'Miguel'}
	return render_template('home.html', title='Home', user=user) 

@app.route('/members')
def members():
  members = Member.query.all()
  results_count = len(members)
  return render_template('members.html', title='Members', members=members, results_count=results_count) 

@app.route('/collections')
def collections():
  return render_template('collections.html', title='Collections') 

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/')
    return render_template('login.html', 
                           title='Sign In',
                           form=form)