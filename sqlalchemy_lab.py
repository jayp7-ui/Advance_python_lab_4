from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Create database
engine = create_engine('sqlite:///data.db')
Base = declarative_base()

# Define table as class
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    course = Column(String)

# Create table
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Insert multiple users
users = [
    User(name="BE Computer", email="be@ncit.edu", course="Engineering"),
    User(name="BSc CSIT", email="csit@ncit.edu", course="Science"),
    User(name="BIT", email="bit@ncit.edu", course="IT"),
]

session.add_all(users)
session.commit()

# Read
print("\nAll Users:")
for user in session.query(User).all():
    print(user.id, user.name, user.email, user.course)

# Update one
user = session.query(User).filter_by(name='BIT').first()
user.course = "Information Technology"
session.commit()

print("\nAfter Update:")
print(session.query(User).filter_by(name='BIT').first().course)

# Delete one
user = session.query(User).filter_by(name='BSc CSIT').first()
session.delete(user)
session.commit()

print("\nAfter Deletion:")
for user in session.query(User).all():
    print(user.id, user.name, user.course)
