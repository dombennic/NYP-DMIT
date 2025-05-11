from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)


class Users(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        args = parser.parse_args()
        
   # load in the classifier and vectorizer from the c drive
    
         data = pd.read_csv('users.csv')

        result = -1
        for idx in data.index:
            if (data['name'][idx] == args['name']):
                result = idx;
        
        if (result != -1):
            return data.loc[result].to_json(),201
        else:
            return '{result:"not found"}',201
        
        #return data['city'][result], 201
        # return {'age' : 30}, 201    
        

    

# Add URL endpoints
api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run()
