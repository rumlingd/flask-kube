import csv
from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import Person


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    """ Method to recreate a database
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed_db')
def seed_db():
    """Command line argument to seed db with titanic csv

    Method loops over a csv file skipping first row and inserting values into
    respective rows.
    O, 1 for survived variable is converted to a boolean type.
    """

    with open('titanic.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row.
        for row in reader:
            survived_bool = None
            if row[0] == '1':
                survived_bool = True

            elif row[0] == '2':
                survived_bool = False

            db.session.add(Person(
                                survived=survived_bool,
                                passengerClass=row[1],
                                name=row[2],
                                sex=row[3],
                                age=int(float(row[4])),
                                siblingsOrSpousesAboard=row[5],
                                parentsOrChildrenAboard=row[6],
                                fare=row[7]
                                ))

    db.session.commit()


if __name__ == '__main__':
    cli()
