from app import db
from datetime import datetime


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
        return '%s, %s %s' % (self.last_name, self.first_name, self.middle_initial)

    def get_url():
        pass
    
    def to_json():
        pass

class CollectionTransaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))
    or_number = db.Column(db.Integer, index=True)
    transaction_date = db.Column(db.DateTime, default=datetime.utcnow)



