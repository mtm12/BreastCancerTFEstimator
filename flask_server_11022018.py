from keras.models import load_model
import tensorflow as tf
import numpy as np
import pandas as pd
import ip_address
from flask import Flask, abort, jsonify, request

app = Flask(__name__)
irisModel = None
bcModel = None

@app.route("/iris/api", methods=['POST'])
def make_predict():
	data = request.get_json(force=True)
	predict_request = [data['sl'],data['sw'],data['pl'],data['pw']]
	predict_request = np.array([predict_request])
	y_pred = irisModel.predict(predict_request)
	return jsonify({'setosa': str(y_pred[0][0]),
		'versicolor': str(y_pred[0][1]),
		'virginica': str(y_pred[0][2])}), 201
		
@app.route("/bc/api", methods=['POST'])
def bc_make_predict():

	data = request.get_json(force=True)
	predict_request = [data['clump_t'],data['size_u'],data['shape_u'],data['marginal_a'],
		data['epithelial_s'], data['bare_n'], data['bland_c'], data['normal_n'],
		data['mitoses']]
		
	#print(predict_request)
	#print(predict_request[1])
	
	inputs = pd.DataFrame({
		'clump_thickness': [int(predict_request[0])],
		'size_uniformity': [int(predict_request[1])],
		'shape_uniformity': [int(predict_request[2])],
		'marginal_adhesion': [int(predict_request[3])],
		'epithelial_size': [int(predict_request[4])],
		'bare_nucleoli': [int(predict_request[5])],
		'bland_chromatin': [int(predict_request[6])],
		'normal_nucleoli': [int(predict_request[7])],
		'mitoses': [int(predict_request[8])],
	})
	
	#print(inputs)

	 # Convert input data into serialized data strings.
	data = []
	for index, row in inputs.iterrows():
		feature = {}
		for col, value in row.iteritems():
			 feature[col] = tf.train.Feature(float_list=tf.train.FloatList(value=[value]))
		data2 = tf.train.Example(
			 features=tf.train.Features(
				 feature=feature
			 )
		 )
		data.append(data2.SerializeToString())

	 # Make predictions.
	predictions = predict_fn({'inputs': data})
	
	#print(predictions['scores'][0][0])
	
	return jsonify({'benign': str(predictions['scores'][0][0]),
		'malignant': str(predictions['scores'][0][1])}), 201
	
@app.route("/test/api")
def hello():
	a = "20"
	return jsonify({'value': a}), 201

if __name__=='__main__':
	print("loading iris model")
	irisModel = load_model('iris_model.h5')
	print("iris model loaded")
	print("loading bc model")
	predict_fn = tf.contrib.predictor.from_saved_model("./bc")
	print("bc model loaded")
	app.run(host=ip_address.ip_address, port=5000)