from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route("/get_locations_names", methods=["GET"])
def get_locations_names():
    response = jsonify({
        "locations": util.get_locations_names()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/predict_home_price", methods=["POST"])
def predict_home_price():
    data = request.get_json()
    location = data['location']
    total_sqft = float(data['total_sqft'])
    bath = int(data['bath'])
    bhk = int(data['bhk'])
    try:
        estimated_price = util.get_estimated_price(location, total_sqft, bath, bhk)
        response = jsonify({"estimated_price": estimated_price})
    except ValueError as e:
        response = jsonify({"error": str(e)})
        response.status_code = 400  # Bad Request
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response