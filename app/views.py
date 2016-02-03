from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
def index():
	user = {'nickname': 'Miguel'}
	return render_template('home.html', title='Home', user=user) 

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