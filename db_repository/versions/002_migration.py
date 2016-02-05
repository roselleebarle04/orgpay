from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
member = Table('member', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('student_id', String(length=10)),
    Column('last_name', String(length=64)),
    Column('first_name', String(length=64)),
    Column('middle_initial', String(length=10)),
    Column('full_name', String(length=150)),
    Column('student_level', Integer),
    Column('student_major', String(length=64)),
    Column('program_department', String(length=64)),
    Column('department_college', String(length=64)),
    Column('gender', String(length=1)),
    Column('registration_date', DateTime),
    Column('scholarship_description', String(length=64)),
    Column('student_permanent_address', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['member'].columns['full_name'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['member'].columns['full_name'].drop()
