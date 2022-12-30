from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sys
sys.path.append('c:/Users/Chayma/OneDrive/Bureau/Test/')
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
        'agent_fullname',
        type=str,
        required=True,
        help="This field cannot be left blank")       


    def get(self, location):
        property = PropertyModel.find_by_location(location)
        if property:
            return property.json()
        return {'message': 'Property not found'}, 404

    def post(self):
        data = Property.parser.parse_args()

        property = PropertyModel(**data)
        try:
            property.save_to_db()
        except:
            return {'message': 'An error occurred while creating the property'}, 500

        return property.json(), 201     

    def delete(self, location):
        property = Property.find_by_name(location)

        if property:
            property.delete_from_db()
            return {'message': 'Property deleted'}
        return {'message': "A property with name '{}' does not exist.".format(location)}, 404

    def put(self, location):
        data = Property.parser.parse_args()

        property = PropertyModel.find_by_name(location)

        if property is None:
            property = PropertyModel(location, **data)
        else:
            property.location = data['location']
            property.type = data['type']
            property.floor = data['floor']
            property.price = data['price']
            property.bed = data['bed']
            property.bath = data['bath']
            property.kitchen = data['kitchen']
            property.garage = data['garage']
            property.agent_fullname = data['agent_fullname']            

        property.save_to_db()

        return property.json()      


class PropertyList(Resource):
    def get(self):
        return PropertyModel.query.all()
        #return {'properties': [property.json() for property in PropertyModel.query.all()]}
        #return {'properties': [x.json() for x in  PropertyModel.query.all()]}
    # def get(self, location):
    #     properties = PropertyModel.query.filter_by(location=location).all()
    #     return properties