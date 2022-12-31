from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sys
sys.path.append('c:/Users/Chayma/OneDrive/Bureau/Real Estate API/')
from models.property import PropertyModel


class Property(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'location',
        type=str,
        required=True,
        help="This field cannot be left blank")    
    parser.add_argument(
        'type',
        type=str,
        required=True,
        help="This field cannot be left blank")
    parser.add_argument(
        'floor',
        type=int,
        required=True,
        help="This field cannot be left blank")
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank")
    parser.add_argument(
        'bed',
        type=int,
        required=True,
        help="This field cannot be left blank")
    parser.add_argument(
        'bath',
        type=int,
        required=True,
        help="This field cannot be left blank")
    parser.add_argument(
        'kitchen',
        type=int,
        required=True,
        help="This field cannot be left blank")
    parser.add_argument(
        'garage',
        type=int,
        required=True,
        help="This field cannot be left blank") 
    parser.add_argument(
        'agent',
        type=str,
        required=True,
        help="This field cannot be left blank")  
    parser.add_argument(
        'phone',
        type=int,
        required=True,
        help="This field cannot be left blank") 
    parser.add_argument(
        'review',
        type=str,
        required=False,
        help="This field cannot be left blank")    

    #Create a property
    def post(self):
        data = Property.parser.parse_args()

        property = PropertyModel(**data)

        try:
            property.save_to_db()
        except:
            return {'message': 'An error occurred while creating the property'}, 500

        return property.json(), 201     


class PropertyID(Resource):

    #Get a specific property by id
    def get(self, id):
        property = PropertyModel.query.filter_by(id=id).first()
        if property:
            return property.json(), 201  
        return {'message': 'Property not found'}, 404

    #Delete an existing property
    def delete(self, id):
        property = PropertyModel.query.filter_by(id=id).first()
        if property:
            property.delete_from_db()
            return {'message': 'Property deleted'}
        return {'message': 'Property not found'}, 404

    #Update a specific property
    def put(self, id):
        data = Property.parser.parse_args()

        property = PropertyModel.query.filter_by(id=id).first()

        if property is None:
            return {'message': 'Property not found'}, 404
        else:
            property.location = data['location']
            property.type = data['type']
            property.floor = data['floor']
            property.price = data['price']
            property.bed = data['bed']
            property.bath = data['bath']
            property.kitchen = data['kitchen']
            property.garage = data['garage']
            property.agent = data['agent'] 
            property.phone = data['phone']
            property.review = data['review']            

        property.save_to_db()
        return property.json()      


class PropertyReview(Resource):
    #Update/Post a Review on a specific Property
    def put(self, id):
        data = request.get_json()
        review = data.get('review')

        property = PropertyModel.query.filter_by(id=id).first()
        if property:
            property.review = review
            property.save_to_db()
            return {'message': 'Review updated successfully'}, 200
        return {'message': 'Property not found'}, 404

class PropertyList(Resource):

    #Get all properties
    def get(self):
        properties = PropertyModel.query.all()
        return [property.json() for property in properties]


class PropertyListPrice(Resource):
    #Get all properties with a specific range of price
    def get(self):
        min_price = request.args.get('min_price')
        max_price = request.args.get('max_price')
        if min_price and max_price:
            properties = PropertyModel.find_by_price_range(min_price, max_price)
            return {'properties': [property.json() for property in properties]}
        return {'properties': [property.json() for property in PropertyModel.query.all()]}


class PropertyListLocation(Resource):

    #Get all roperties in a specific location
    def get(self, location):
        properties = PropertyModel.find_by_location(location)
        return [property.json() for property in properties]


class PropertyListLocationPrice(Resource):
    #Get all properties with a specific range of price and a specific range
    def get(self):
        location = request.args.get('location')
        min_price = request.args.get('min_price')
        max_price = request.args.get('max_price')
        
        properties = PropertyModel.find_by_location_and_price(location, min_price, max_price)
        if properties:
            return {'properties': [property.json() for property in properties]}, 200
        return {'message': 'No properties found in this location with the specified price range'}, 404