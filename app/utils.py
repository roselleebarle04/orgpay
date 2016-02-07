import csv
import datetime
from datetime import datetime, date
from app import db
from app.models import *


def convert_string_to_date(date_str):
	""" Format should be: mm/dd/yy - Clean date data from csv - convert string to datetime object """

	d = date_str.split('/')
	month = int(d[0])
	day = int(d[1])
	year = int(d[2])
	d = date(year, month, day)
	return d

def create_name_object(name_str):
	names = name_str.split(',')
	name = {}
	name['first'] = unicode(names[0], 'utf-8')
	name['last'] = unicode(names[1][:-3], 'utf-8')
	name['middle'] = unicode(names[1][-2:-1], 'utf-8')
	return name

def bulk_add_members(filename):
	""" Data is provided by official authorities (registrar) """ 

	f = open(filename)
	reader = csv.reader(f)

	arr_members = []
	for row in reader:
		student_id = row[1]
		print "Adding student #%s" % (student_id)

		name = create_name_object(row[2])

		student_level = int(row[3])
		student_major = row[4]
		program_department = row[5] 
		department_college = row[6] 

		gender = row[7]
		registration_date = convert_string_to_date(row[8])

		scholarship_description = row[9] 
		student_permanent_address = unicode(row[10], 'utf-8') 

		member = Member(student_id=student_id, last_name=name['last'], first_name=name['first'], middle_initial=name['middle'], student_level=student_level, student_major=student_major, program_department=program_department, department_college=department_college, gender=gender, registration_date=registration_date, scholarship_description=scholarship_description, student_permanent_address=student_permanent_address)
		arr_members.append(member)
		db.session.add(member)
		db.session.commit()

def bulk_add_collection_transactions(filename):
	""" Data is provided by the organization's spreadsheet/record/log 
	Will be used when data is properly formatted. No data available yet. """
	pass

def initialize_db():
	db.create_all()

def destroy_db():
	db.drop_all()

def add_test_member():
	member = Member(student_id=20130038)
	db.session.add(member)
	db.session.commit()

def add_test_collection_category():
	category = CollectionCategory(name='MAF')
	db.session.add(category)
	db.session.commit()

def add_test_collection_transaction():
	transaction = CollectionTransaction(member_id=Member.query.get(id=1), or_number=123456)
	# How to add collectionitems in collectiontransaction? 

def call_bulk_add():
	filenames = ['cass.csv', 'cbaa.csv', 'ced.csv', 'coe.csv', 'con.csv', 'csm.csv', 'csm-graduate.csv', 'scs.csv', 'set.csv', 'sgs.csv']
	for filename in filenames:
		data_dir = 'data/'
		csv_dir = data_dir + filename
		bulk_add_members(csv_dir)

def add_test_data():
	destroy_db()
	initialize_db()
	add_test_member()