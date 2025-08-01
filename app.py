from flask import Flask, jsonify
from model import load_matches

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    predictions = load_matches()
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)
