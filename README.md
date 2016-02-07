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
$ python db_create.py
$ python db_migrate.py
$ python
>> from app.utils import add_test_data
>> add_test_data()
>> ctrol+d

#### Used Packages

- SQLAlchemy-migrate for migrations
- Flask-RESTful for implementing REST Apis
- Nosetests - For testing

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
