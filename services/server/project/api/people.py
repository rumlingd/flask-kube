import uuid

from flask import Blueprint, jsonify, request

from project.api.models import Person
from project import db


people_blueprint = Blueprint('people', __name__)


@people_blueprint.route('/api/v1/people', methods=['GET', 'POST'])
def all_people():
    """
    This function responds to a request for /api/v1/people
    with the complete lists of people if a GET Request is sent.

    A POST Request with the correct payload creates a new person
    e.g:
    {"survived": true, "passengerClass": 3, "name": "Mr. Owen Harris Braund",
    "sex": "male", "age": 22, "siblingsOrSpousesAboard": 1,
    "parentsOrChildrenAboard":0, "fare":7.25}
    """

    if request.method == 'POST':
        post_data = request.get_json()
        survived = post_data.get('survived')
        passengerClass = post_data.get('passengerClass')
        name = post_data.get('name')
        sex = post_data.get('sex')
        age = post_data.get('age')
        siblingsOrSpousesAboard = post_data.get('siblingsOrSpousesAboard')
        parentsOrChildrenAboard = post_data.get('parentsOrChildrenAboard')
        fare = post_data.get('fare')

        person_to_add = Person(survived=survived,
                               passengerClass=passengerClass,
                               name=name, sex=sex, age=age,
                               parentsOrChildrenAboard=parentsOrChildrenAboard,
                               siblingsOrSpousesAboard=siblingsOrSpousesAboard,
                               fare=fare)

        db.session.add(person_to_add)
        db.session.commit()
        response_object = person_to_add.to_json()
    else:
        response_object = [person.to_json() for person in Person.query.all()]
    return jsonify(response_object)


@people_blueprint.route('/api/v1/people/<uuid>', methods=['PUT', 'DELETE', 'GET'])
def single_person(uuid):
    """
    This function responds to a request for /api/people/<uuid>
    
    A PUT Request with the correct payload creates update a person
    A GET Request returns details on person with a certain uuid
    A DELETE Request removes a person with a certain uuid
    """

    person = Person.query.filter_by(id=uuid).first()

    if request.method == 'PUT':
        post_data = request.get_json()
        person.survived = post_data.get('survived')
        person.passengerClass = post_data.get('passengerClass')
        person.name = post_data.get('name')
        person.sex = post_data.get('sex')
        person.age = post_data.get('age')
        person.siblingsOrSpousesAboard = post_data.get(
                                         'siblingsOrSpousesAboard')

        person.parentsOrChildrenAboard = post_data.get(
                                         'parentsOrChildrenAboard')

        person.fare = post_data.get('fare')
        db.session.commit()
        response_object = person.to_json()

    if request.method == 'DELETE':
        db.session.delete(person)
        db.session.commit()
        response_object = 'Person removed!'

    if request.method == 'GET':
        person = Person.query.filter_by(id=uuid).first()
        db.session.commit()
        response_object = person.to_json()

    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
