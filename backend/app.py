from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'



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
  
        return jsonify(data)
    
if __name__ == '__main__':
    app.run(debug=True)