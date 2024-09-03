from lib2to3.pytree import Base
from sqlalchemy import Table, Text, ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# association table
post_keywords = Table('post_keywords', Base.metadata,
                      Column('post_id', ForeignKey('posts.id'), primary_key=True),
                      Column('keyword_id', ForeignKey('keywords.id'), primary_key=True)
)

class BlogPost(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    headline = Column(String(255), nullable=False)
    body = Column(Text)

    # many to many BlogPost<-> Keyword
    Keywords = relationship('Keyword',
                            secondary=post_keywords,
                            back_populates='posts')
    
    # one to many Blogpost -> Comment
    def __init__(self, headline, body, author):
        self.author = author
        self.headline = headline
        self.body = body
    
    def __repr__(self):
        return "BlogPost(%r, %r, %r)" % (self.headline, self.body, self.author)

# Keyword class
class Keyword(Base):
    __tablename__ = 'Keywords'

    id = Column(Integer, primary_key=True)
    Keyword = Column(String(50), nullable=False, unique=True)
    posts = relationship('BlogPost',
                         secondary=post_keywords,
                         back_populates='Keywords')
    
    # Initialize the keyword
    def __init__(self, keyword):
        self.Keyword = keyword
