from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from camera import takePicture

app = Flask(__name__)
# Enable CORS
CORS(app)

@app.route("/binbin/camera", methods=["POST"])
def predict():
	
	if request.method == "POST":   
		print("Oh Noooooo") 		
		takePicture('test.jpg')
        
	return jsonify(
		prediction= "Nani"
	),201