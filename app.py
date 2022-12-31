from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT
from datetime import timedelta

from security import authenticate, identity
from resources.user import UserRegister
from resources.property import Property, PropertyList, PropertyID, PropertyListLocation, PropertyListLocationPrice, PropertyListPrice, PropertyReview
from db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.secret_key = 'chayma'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

#Change the by default '/auth to /login
app.config['JWT_AUTH_URL_RULE'] = '/login'
jwt = JWT(app, authenticate, identity) #/auth

#Configure JWT to expire within half an hour
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)

@jwt.auth_response_handler
def customized_response_handler(access_token, identity):
    return jsonify({
        'access_token': access_token,
        'user_id': identity.id,
        'expire within': '30 min'
        }
    )

@jwt.jwt_error_handler
def customized_error_handler(error):
    
    return jsonify({
        'message': error.description,
        'code': error.status_code
        }), error.status_code

api.add_resource(Property, '/property/')
api.add_resource(PropertyID, '/property/<int:id>')
api.add_resource(PropertyReview, '/property/review/<int:id>')
api.add_resource(PropertyList, '/properties')
api.add_resource(PropertyListLocation, '/properties/location/<string:location>')
api.add_resource(PropertyListPrice, '/properties/price')
api.add_resource(PropertyListLocationPrice, '/properties/location/price')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)