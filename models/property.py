import sys
sys.path.append('c:/Users/Chayma/OneDrive/Bureau/Test/')
from db import db

class PropertyModel(db.Model):
    __tablename__ = "properties"
    
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(80))
    type = db.Column(db.String(80)) 
    floor = db.Column(db.Integer)
    price = db.Column(db.Float) 
    bed = db.Column(db.Integer) 
    bath = db.Column(db.Integer) 
    kitchen = db.Column(db.Integer)
    garage = db.Column(db.Integer)  

    agent_fullname = db.Column((db.String(80)), db.ForeignKey('agents.full_name')) 
    agent = db.relationship('AgentModel')

    def __init__(self, location, type, floor, price, bed, bath, kitchen, garage, agent_fullname):
        self.location = location
        self.type = type
        self.floor = floor
        self.price = price
        self.bed = bed
        self.bath = bath
        self.kitchen = kitchen
        self.garage = garage
        self.agent_fullname = agent_fullname

    def json(self):
        return {
            'location': self.location,
            'type': self.type,
            'floor': self.floor,
            'price': self.price,
            'bed': self.bed,
            'bath': self.bath,
            'kitchen': self.kitchen,
            'garage': self.garage,
            'agent': self.agent            
        }
    
    @classmethod
    def find_by_location(cls, location):
        return cls.query.filter_by(location=location).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit() 

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()