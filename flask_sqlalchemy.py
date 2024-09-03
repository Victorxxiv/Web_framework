from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Create an engine that stores data in the local directory's
engine = create_engine('sqlite:///:memory:', each=True)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define a User class
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

# Define a __repr__ method for the User class
    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)

# Define an Address class, mapping relationship to the User class
class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    # Relationship with User
    user = relationship("User", back_populates="addresses")

    # Define a __repr__ method for the Address class
    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

# Add a relationship from User to Address
User.addresses = relationship(
    "Address", order_by=Address.id, back_populates="user")
