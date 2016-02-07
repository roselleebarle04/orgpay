from app import db
from datetime import datetime
from flask import url_for

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(db.String(10), unique=True, index=True)
    last_name = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    middle_initial = db.Column(db.String(10))
    full_name = db.Column(db.String(150))

    student_level = db.Column(db.Integer)
    student_major = db.Column(db.String(64))
    program_department = db.Column(db.String(64))
    department_college = db.Column(db.String(64))

    gender = db.Column(db.String(1))
    registration_date = db.Column(db.DateTime)
    scholarship_description = db.Column(db.String(64))
    student_permanent_address = db.Column(db.String(120))
    
    collectiontransactions = db.relationship('CollectionTransaction', backref='member')

    def __repr__(self):
        return '%s' % (self.id)

    def get_url(self):
        return url_for('get_member', id=self.id, _external=True)
    
    def to_json(self):
        return {
            'url': self.get_url(),
            'student_id': self.student_id,
            'names': {
                'last_name': self.last_name,
                'first_name': self.first_name,
                'middle_initial': self.middle_initial,
            }, 
            'student_level': self.student_level,
            'student_major': self.student_major,
            'program_department': self.program_department, 
            'department_college': self.department_college, 
            'gender': self.gender, 
            'registration_date': self.registration_date,
            'scholarship_description': self.scholarship_description, 
            'address': self.student_permanent_address,

            'collections': url_for('get_member_collections', id=self.id, _external=True)
        }

class ValidationError(ValueError):
    pass

class CollectionTransaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))
    or_number = db.Column(db.Integer, index=True)
    transaction_date = db.Column(db.DateTime, default=datetime.utcnow)

    def get_url(self):
        return url_for('get_collection', id=self.id, _external=True)

    def to_json(self):
        return {
            'url': self.get_url(),
            'member': url_for('get_member', id=self.member_id, _external=True),
            'or_number': self.or_number,
            'transaction_date': self.transaction_date,
        }

    def from_json(self, json):
        try:
            self.member_id = json['member_id']
            self.or_number = json['or_number']
        except KeyError as e:
            raise ValidationError('Invalid Or Number: Missing ' + e.args[0])
        return self
