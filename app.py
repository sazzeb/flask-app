# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

menu = [
    {"id": 1, "name": "Burger", "price": 10},
    {"id": 2, "name": "Pizza", "price": 12},
    {"id": 3, "name": "Salad", "price": 8},
]

orders = []


@app.route("/menu", methods=["GET"])
def get_menu():
    return jsonify(menu)


@app.route("/order", methods=["POST"])
def place_order():
    data = request.get_json()
    order = {"items": data["items"], "total": sum(item["price"] for item in data["items"])}
    orders.append(order)
    return jsonify({"message": "Order placed successfully"})


@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

