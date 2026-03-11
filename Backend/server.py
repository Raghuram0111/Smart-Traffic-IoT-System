from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# DATABASE CONNECTION
client = MongoClient("mongodb://localhost:27017/")

db = client["smart_traffic_db"]
collection = db["traffic_data"]

@app.route('/')
def home():
    return "Smart Traffic IoT Server Running"

# STORE DATA
@app.route('/traffic', methods=['POST'])
def receive_data():

    data = request.json

    if data["vehicle_count"] > 80:
        data["status"] = "High Traffic"
    else:
        data["status"] = "Normal"

    collection.insert_one(data)

    return jsonify({"message":"Traffic data stored"})

# FETCH DATA
@app.route('/gettraffic', methods=['GET'])
def get_traffic():

    data = list(collection.find({},{"_id":0}))

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)