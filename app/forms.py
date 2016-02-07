from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Required
from .models import CollectionTransaction

class CollectionTransactionForm(Form):
    member_id = SelectField('Member', validators=[Required()])
    or_number = IntegerField('Or Number', validators=[Required()])
    submit = SubmitField('Submit')


# class LoginForm(Form):
#     openid = StringField('openid', validators=[DataRequired()])
#     remember_me = BooleanField('remember_me', default=False)

