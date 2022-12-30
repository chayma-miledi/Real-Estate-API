import sys
sys.path.append('c:/Users/Chayma/OneDrive/Bureau/Test/')
from db import db

class AgentModel(db.Model):
    __tablename__ = "agents"
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80)) 
    location = db.Column(db.String(80)) 
    phone = db.Column(db.Integer) 

    properties = db.relationship('PropertyModel', lazy='dynamic')

    def __init__(self, full_name, location, phone):
        self.full_name = full_name
        self.location = location
        self.phone = phone

    def json(self):
        return {
            'full_name': self.full_name,
            'location': self.location,
            'phone': self.phone,
            'properties': [property.json() for property in self.properties.all()]
        }
    @classmethod
    def find_all(cls):
        return cls.query.all()
        
    @classmethod
    def find_by_name(cls, full_name):
        return cls.query.filter_by(full_name=full_name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit() 

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()