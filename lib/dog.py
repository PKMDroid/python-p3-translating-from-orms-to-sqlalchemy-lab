# lib/dog.py
from models import Dog, Base, engine, session

def create_table(Base, engine):
    """Create the table for the Dog model"""
    Base.metadata.create_all(engine)

def save(session, dog):
    """Save a Dog instance to the database"""
    session.add(dog)
    session.commit()
    return dog

def get_all(session):
    """Return all Dog instances from the database"""
    return session.query(Dog).all()

def find_by_name(session, name):
    """Return a Dog instance by name"""
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    """Return a Dog instance by id"""
    return session.query(Dog).get(id)

def find_by_name_and_breed(session, name, breed):
    """Return a Dog instance matching name and breed"""
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, new_breed):
    """Update a Dog instance's breed"""
    dog.breed = new_breed
    session.commit()
    return dog
