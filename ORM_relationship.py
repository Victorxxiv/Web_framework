from sqlalchemy import Table, Text

# association table
post_keywords = Table('post_keywords', Base.metadata,
                      Column('post_id', ForeignKey('posts.id'), primary_key=True),
                      Column('keyword_id', ForeignKey('keywords.id'), primary_key=True)
)
