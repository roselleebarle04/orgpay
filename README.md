## Organization Management System

Integrated workflow for Collections/Payments/Cashiering Module, Memberships, Events, Liquidations, Inventory, Insurance in any organizations.

#### Local Installation

````
# Use virtualenvwrapper
mkvirtualenv orgpay

pip install -r requirements.txt
python run.py
````

#### Add Dummy Data
````
$ python db_create.py
$ python db_migrate.py
$ python
>> from app.utils import add_test_data
>> add_test_data()
>> ctrol+d
````

#### Used Packages

- SQLAlchemy-migrate for migrations
- Flask-RESTful for implementing REST Apis
- Nose - For testing
- Flask-HTTPAuth

#### Notes
- SQLAlchemy(http://www.sqlalchemy.org/) - Python SQL toolkit and Object Relational Mapper 

#### References
- https://github.com/mitsuhiko/flask/wiki/Large-app-how-to
- https://blog.openshift.com/build-your-app-on-openshift-using-flask-sqlalchemy-and-postgresql-92/
- http://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful
- http://shop.oreilly.com/product/0636920034803.do
- http://blog.miguelgrinberg.com/post/writing-a-javascript-rest-client
- http://flask.pocoo.org/docs/0.10/tutorial/

#### Resources
- http://www.fullstackpython.com/flask.html
- https://exploreflask.com/index.html

## Ultimate Guide

Project Orgpay - Using Flask/Flask-SQLAlchemy/Flask-RESTful/AngularJS

Integrated workflow for Collections/Payments/Cashiering Module, Memberships, Events, Liquidations, Inventory, Insurance in any organizations.

A comprehensive guide in creating a restful application using Flask, Flask-RESTful, AngularJS, and Flask-SQLAlchemy

#### Outline
- Preliminary Discussions
- Setup Virtualenvironment
- Initialize Application

#### Set up virtualenvironment
````
pip install virtualenv
pip install virtualenvwrapper
sudo nano ~/.bashrc: 

# Add the following lines in the end of your file
>> source '/usr/local/bin/virtualenvwrapper.sh'

# Reactivate bash file
sudo ~/.bashrc

# Create virtualenv
mkvirtualenv orgpay
````

#### Initialize Flask Application

App Folder Structure / Overview
````
/orgpay
..../orgpay
......../static
......../templates
........__init__.py
....run.py
....db.py
````