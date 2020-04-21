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


class Class(DatabaseModel):
    __tablename__ = "class"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    profile = Column(String(100), default="")
    students = relationship("Student", backref="class")


class Student(DatabaseModel):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    class_id = Column(Integer, ForeignKey("class.id"))


DatabaseModel.metadata.create_all(database)
