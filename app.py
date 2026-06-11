from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# TODO: Implement homepage route that returns a welcome message

@app.route("/")
def home():
    return jsonify({"message": "Welcome"})  # TODO: Return a welcome message

# TODO: Implement GET /products route that returns all products or filters by category

@app.route("/products")
def get_products():
    category = request.args.get("category")
    if category:
        filtered = [c for c in products if c["category"] == category]
        return jsonify(filtered), 200
    return jsonify(products), 200  # TODO: Return all products or filter by ?category=

# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404

@app.route("/products/<int:id>")
def get_product_by_id(id):
    for product in products:
        if product["id"] == id:
            return jsonify(product), 200
    return jsonify({"message": "Product not found"}), 404  # TODO: Return product by ID or 404

if __name__ == "__main__":
    app.run(debug=True)
