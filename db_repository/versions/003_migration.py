from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
collectionTransactionItems = Table('collectionTransactionItems', pre_meta,
    Column('collectiontransaction_id', INTEGER),
    Column('collectionitem_id', INTEGER),
)

collection_category = Table('collection_category', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
)

collection_item = Table('collection_item', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('amount', INTEGER),
    Column('is_required', BOOLEAN),
    Column('collectioncategory_id', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['collectionTransactionItems'].drop()
    pre_meta.tables['collection_category'].drop()
    pre_meta.tables['collection_item'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['collectionTransactionItems'].create()
    pre_meta.tables['collection_category'].create()
    pre_meta.tables['collection_item'].create()
