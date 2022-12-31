import sys
sys.path.append('c:/Users/Chayma/OneDrive/Bureau/Real Estate API/')
from db import db

class PropertyModel(db.Model):
    __tablename__ = "properties"
    
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(80))
    type = db.Column(db.String(80)) 
    floor = db.Column(db.Integer)
    price = db.Column(db.Integer) 
    bed = db.Column(db.Integer) 
    bath = db.Column(db.Integer) 
    kitchen = db.Column(db.Integer)
    garage = db.Column(db.Integer)  
    agent = db.Column(db.String(80))
    phone = db.Column(db.Integer)
    review = db.Column(db.String)

    def __init__(self, location, type, floor, price, bed, bath, kitchen, garage, agent, phone, review):
        self.location = location
        self.type = type
        self.floor = floor
        self.price = price
        self.bed = bed
        self.bath = bath
        self.kitchen = kitchen
        self.garage = garage
        self.agent = agent
        self.phone = phone
        self.review = review

    def json(self):
        return {
            'id': self.id,
            'location': self.location,
            'type': self.type,
            'floor': self.floor,
            'price': self.price,
            'bed': self.bed,
            'bath': self.bath,
            'kitchen': self.kitchen,
            'garage': self.garage,
            'agent': self.agent,
            'phone': self.phone,
            'review': self.review           
        }
    
    @classmethod
    def find_by_location(cls, location):
        return cls.query.filter_by(location=location).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit() 

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_price_range(cls, min_price, max_price):
        return cls.query.filter(cls.price.between(min_price, max_price)).all()

    @classmethod
    def find_by_location_and_price(cls, location, min_price, max_price):
        return cls.query.filter(cls.location == location, cls.price.between(min_price, max_price)).all()