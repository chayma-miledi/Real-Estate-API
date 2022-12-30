from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sys
sys.path.append('c:/Users/Chayma/OneDrive/Bureau/Test/')
from models.agent import AgentModel

class Agent(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'location',
        type=str,
        required=True,
        help="This field cannot be left blank")
    parser.add_argument(
        'phone',
        type=int,
        required=True,
        help="This field cannot be left blank")

    @jwt_required()
    def get(self, full_name):
        agent = AgentModel.find_by_name(full_name)
        if agent:
            return agent.json()
        return {'message': "An agent with name '{}' does not exist.".format(full_name)}, 404

    def post(self, full_name):
        if AgentModel.find_by_name(full_name):
            return {'message': "An agent with name '{}' already exists.".format(full_name)}, 400

        data = Agent.parser.parse_args()

        agent = AgentModel(full_name,**data)

        try:
            agent.save_to_db()
        except:
            return {"message": "An error occured when creating the agent."}, 500 #internal server error

        return agent.json(), 201       

    def delete(self, full_name):
        agent = AgentModel.find_by_name(full_name)
        if agent:
            agent.delete_from_db()
            return {'message': 'Agent deleted'}
        return {'message': "An agent with name '{}' does not exist.".format(full_name)}, 404

    def put(self, full_name):
        agent = AgentModel.find_by_name(full_name)
        if not agent:
            return {'message': "An agent with name '{}' does not exist.".format(full_name)}, 404

        data = Agent.parser.parse_args()
        agent.full_name = full_name
        agent.location = data['location']
        agent.phone = data['phone']

        try:
            agent.save_to_db()
        except:
            return {'message': 'An error occurred while updating the agent'}, 500

        return agent.json(),    

class AgentList(Resource):
    def get(self):
        agents = AgentModel.find_all()
        return {'agents': [agent.json() for agent in agents]}
        #return {'agents': [x.json() for x in  AgentModel.query.all()]}