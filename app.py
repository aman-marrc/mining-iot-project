from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data_store = []

def detect(data):
    alerts = []

    if data["speed"] == 0:
        alerts.append("Idle detected")

    if data["lat"] > 24:
        alerts.append("Route deviation")

    return alerts

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    data["alerts"] = detect(data)
    data_store.append(data)
    return {"status": "received"}

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_store)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)