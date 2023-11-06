from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open('complain_forecast.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/test')
def test():
    return 'Hello test'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict(np.array(list(data.values())).reshape(1, -1))
    if prediction == 0:
        return jsonify("not complain")
    else:
        return jsonify("complain")

if __name__ == '__main__':
    app.run(debug=True)