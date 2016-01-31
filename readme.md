1. 

Source: http://techarena51.com/index.php/buidling-a-database-driven-restful-json-api-in-python-3-with-flask-flask-restful-and-sqlalchemy/

pip install Flask Flask-Restful Flask-SQLAlchemy marshmallow marshmallow-jsonapi

from flask import g, Blueprint, jsonify, make_response, request
from flask_restful import Resource, Api
import flask_restful



Notes:
SQLAlchemy(http://www.sqlalchemy.org/) - Python SQL toolkit and Object Relational Mapper 

References:
https://blog.openshift.com/build-your-app-on-openshift-using-flask-sqlalchemy-and-postgresql-92/

http://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful
http://shop.oreilly.com/product/0636920034803.do
http://blog.miguelgrinberg.com/post/writing-a-javascript-rest-client
http://flask.pocoo.org/docs/0.10/tutorial/