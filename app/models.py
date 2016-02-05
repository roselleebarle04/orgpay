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
        return '<Member %r>' % (self.student_id)

collectionTransactionItems = db.Table('collectionTransactionItems',
    db.Column('collectiontransaction_id', db.Integer, db.ForeignKey('collection_transaction.id')),
    db.Column('collectionitem_id', db.Integer, db.ForeignKey('collection_item.id')),
)

class CollectionTransaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))
    transaction_date = db.Column(db.DateTime) 
    or_number = db.Column(db.Integer, index=True)
    collection_items = db.relationship('CollectionItem', 
        secondary=collectionTransactionItems, 
        backref=db.backref('collectiontransactions', lazy='dynamic'), 
        lazy='dynamic')

    def get_total(self, collectiontransaction):
        return 0 

class CollectionItem(db.Model):
    """ This model serves as the association table between the many-to-many
    relationsip between Member and CollectionTransaction"""
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    is_required = db.Column(db.Boolean)
    collectioncategory_id = db.Column(db.Integer, db.ForeignKey('collection_category.id'))

class CollectionCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    
    collectionitems = db.relationship('CollectionItem', backref='collectioncategory')



