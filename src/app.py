# Gabriel Carvalho
from flask import Flask, request, jsonify
import sys

app = Flask(__name__)

products = [
    {"name": "Apple", "price": 1.20, "amount": 3500},
    {"name": "Peach", "price": 5.50, "amount": 600},
    {"name": "Banana", "price": 0.98, "amount": 340}
]

@app.route("/products", methods=["get"])
def get_products():
    """
    Get all products
    """
    return jsonify(products)


@app.route("/new_product", methods=["post"])
def create_product():
    """
    create new product
    """
    new_product = request.json
    products.append(new_product)
    return jsonify(new_product), 201


if __name__ == "__main__":
    app.run(debug=True)
    sys.exit(0)