from flask import Blueprint, Flask, request, make_response, jsonify
from flask_restplus import Api, Resource

from app.api.v1.models import products

app = Flask(__name__)
api = Api(app)

api_prods = Blueprint('api_prods', __name__)
api_prod = Blueprint('api_prod', __name__)

@api.route('/products')
class Products(Resource):
	def get(self):
		if len(products) != 0 :
			return {"Products" : products}, 200
		return {"Message":"There are no products in stock."}

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
		    "price" : float(price)
		}

		products.append(new_product)

		return {"Message" : "Product added successfully", "Products":products}, 200


@api.route('/product/<int:id>')
class Product(Resource):
	def get(self, id):
		single_product = [product for product in products if product['id'] == id]
		return {"Product" : single_product}, 200