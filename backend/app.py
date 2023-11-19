from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import os
import prediction

app = Flask(__name__)

cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

class GetDiseasePrediction(Resource):
    def get(self):
        return 'Welcome to Health Detective'
    
    def post(self):
        try:
            data = request.get_json()

            predictResult = prediction.predict_disease(data)

            return {'result':predictResult}
        
        except Exception as error:
            return {'error': error}
    
api.add_resource(GetDiseasePrediction,'/get-disease')

if __name__ == '__main__':
    app.run(debug=True)