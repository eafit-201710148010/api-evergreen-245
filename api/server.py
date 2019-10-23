from flask import Flask, jsonify, request 
from flask_cors import CORS
from api.mediciones import Medicion

app = Flask(__name__)
CORS(app)

medicion_obj = Medicion()

@app.route('/mediciones',methods=['GET'])
def getAll():
    #return (Medicion.list())
    return jsonify(medicion_obj.list())

@app.route('/mediciones',methods=['POST'])
def postOne():
    body = request.json
    #return (Medicion.create(body))
    return medicion_obj.create(body)

app.run(port=5000,debug=True)
