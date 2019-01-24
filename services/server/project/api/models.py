import datetime
from uuid import uuid4
from flask import current_app
from sqlalchemy.sql import func

from project import db


class Person(db.Model):
    """Person class which initiates each row of the db with
        a unique uuid using the standard library
    """

    __tablename__ = 'people'
    id = db.Column(db.String, primary_key=True)
    survived = db.Column(db.Boolean(), default=False, nullable=False)
    passengerClass = db.Column(db.Integer(), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    sex = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    siblingsOrSpousesAboard = db.Column(db.Integer(), nullable=False)
    parentsOrChildrenAboard = db.Column(db.Integer(), nullable=False)
    fare = db.Column(db.Float(), nullable=False)

    def __init__(self, survived, passengerClass, name, sex, age, 
                 siblingsOrSpousesAboard, parentsOrChildrenAboard, fare):

        self.id = str(uuid4())
        self.survived = survived
        self.passengerClass = passengerClass
        self.name = name
        self.sex = sex
        self.age = age
        self.siblingsOrSpousesAboard = siblingsOrSpousesAboard
        self.parentsOrChildrenAboard = parentsOrChildrenAboard
        self.fare = fare

    def to_json(self):
        return {
            'uuid': self.id,
            'survived': self.survived,
            'passengerClass': self.passengerClass,
            'name': self.name,
            'sex': self.sex,
            'age': self.age,
            'siblingsOrSpousesAboard': self.siblingsOrSpousesAboard,
            'parentsOrChildrenAboard': self.parentsOrChildrenAboard,
            'fare': self.fare
        }
