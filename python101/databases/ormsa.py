# Introduction to ORM systems - SQL Alchemy

import os
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# import sqlite3
# con = sqlite3.connect("test.db")

# Delete old database file
if os.path.exists("test.db"):
    os.remove("test.db")

# Create new engine/ instance Engine class to handle a database
# If we put ':memory:' option, we would have our database in RAM memory
database = create_engine("sqlite:///test.db")

# Main/base class for database
DatabaseModel = declarative_base()

# Create a class for each table
# ORM use class to describe fields and relationships between classes(tables)


class ClassGroup(DatabaseModel):
    __tablename__ = "classgroup"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    profile = Column(String(100), default="")
    # this function shows, that table will have constrain with another table
    students = relationship("Student", backref="classgroup")                 # feedback relationship


class Student(DatabaseModel):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    # According ORM system, we define foreign key from other table
    class_id = Column(Integer, ForeignKey("classgroup.id"))


# We execute our defined classes on model, to put tables in our new engine/database
DatabaseModel.metadata.create_all(database)


# Create a session, where we will keep objects and which allow 'conversation' with database
DBSession = sessionmaker(bind=database)
session = DBSession()

# Add two classes, if table will be empty
if not session.query(ClassGroup).count():
    session.add(ClassGroup(name="1A", profile="humanistic"))
    session.add(ClassGroup(name="1B", profile="math"))

# We need to create instance of class, which will be representation of class '1A'
inst_class = session.query(ClassGroup).filter_by(name="1A").one()

# Add also few records to Student table
session.add_all([
    Student(first_name="Sebastian", last_name="Warszawa", class_id=inst_class.id),
    Student(first_name="Grzegorz", last_name="Rogowski", class_id=inst_class.id),
    Student(first_name="Paula", last_name="Jargosz", class_id=inst_class.id)
])


# Print record from student table
def read_data():
    for student in session.query(Student).join(ClassGroup).all():
        print(student.first_name, student.last_name, student.class_id, student.classgroup.name)


read_data()
session.commit()