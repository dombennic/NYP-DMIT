from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import pandas as pd
from sklearn import tree
import json


app = Flask(__name__)
api = Api(app)


class Users(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('weight', required=True)
        parser.add_argument('texture', required=True)
        args = parser.parse_args()
        
  
        features = [[130,1], [140,1], [150,0], [170, 0]]
        labels = [0,0,1,1]
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(features, labels)
        print(args['weight'])
        print(args['texture'])
        # return {'label':clf.predict[160,0]},201
        # return "{'tan Ah Kow'}",201
        # val = input("Enter value for prediction: ")
        # value = input("Enter value for second prediction: ")
        
        answer = clf.predict([[args['weight'],args['texture']]])
        
        lists = answer.tolist()
        json_str = json.dumps(lists)
        print("value should be" + json_str)
        
        return json_str,201
        # return {'label':clf.predict[args['weight'],args['texture']]},201

        
        # return {'age' : 30}, 201    
        

    

# Add URL endpoints
api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run()
