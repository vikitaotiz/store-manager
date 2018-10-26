from flask import Flask, request, Blueprint, make_response, jsonify
from flask_restplus import Resource, Api
# from flask_jwt_extended import JWTManager, jwt_required, get_jwt_claims
from jsonschema import validate

from app.api.v1.models.models import products
from app.api.v1.utils.validate import schema

app = Flask(__name__)
api = Api(app)

api_prods = Blueprint('api_prods', __name__)
api_prod = Blueprint('api_prod', __name__)

@api.route('/api/v1/products')
class Products(Resource):
	def get(self):
		if len(products) != 0 :
			return {"Products" : products}, 200
		return {"Message":"There are no products in stock."}

	# @jwt_required
	def post(self):
		req_data = request.get_json()
		id = len(products) + 1
		name = req_data['name']
		category = req_data['category']
		quantity = req_data['quantity']
		price = req_data['price']

		new_product = {
		    "id" : id,
		    "name" : name,
		    "category" : category,
		    "quantity" : quantity,
		    "price" : price
		}

		if quantity <= 0:
			return jsonify({"Message" : "You can not create product with quantity of zero"})
		validate(new_product, schema)

		# user_role = get_jwt_claims()

		# admin = "admin"

		# if user_role['role'] != admin:
		# 	return jsonify({"message": "Only an admin is permitted to post products"}), 401

		products.append(new_product)

		return {"Message" : "Product added successfully", "Products":products}, 200


@api.route('/api/v1/product/<int:id>')
class Product(Resource):
	# @jwt_required
	def get(self, id):
		single_product = [product for product in products if product['id'] == id]
		return {"Product" : single_product}, 200