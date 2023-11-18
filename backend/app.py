from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/jsonParser', methods=['GET'])
def parseJson():
    if request.method == 'GET':
        file_path = 'emptyJson.json'# you will need to change this to your json file name
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                json_data = file.read()
                return json_data
        else:
            return jsonify({'error': 'File not found'}), 404 

@app.route('/getData', methods=['GET'])
def getData():
    if(request.method == 'GET'): 
        data = { 
            "result" : {
                "matchingDiseases": [
                    "fever", "cold"
                ]
            }
        } 
        print(data)
        return jsonify(data)
    
if __name__ == '__main__':
    app.run(debug=True)