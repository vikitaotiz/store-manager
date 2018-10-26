from flask import Blueprint, request, jsonify
from flask_restplus import Api, Resource
# from flask_jwt_extended import JWTMasnager, jwt_required, get_jwt_claims
from jsonschema import validate

from app.api.v1.models.models import sales
from app.api.v1.models.models import products
from app.api.v1.utils.validate import schema

from app.api.v1.views.products import app, api
api_sales = Blueprint('api_sales', __name__)
api_sale = Blueprint('api_sale', __name__)

@api.route('/api/v1/sales')
class Sales(Resource):
	def get(self):
		if len(sales) != 0 :
			return {"Sales" : sales}, 200
		return {"Message":"There are no sales records in stock."}
		
	# @jwt_required	
	def post(self):
		req_data = request.get_json()
		id = len(sales) + 1
		name = req_data['name']
		category = req_data['category']
		quantity = req_data['quantity']
		price = req_data['price']

		product_name = [product for product in products if product['name'] == name]

		if not product_name:
			return "Product does not exist"
		product_name[0]["quantity"] = product_name[0]["quantity"] - 1
        
		new_sale = {
		  "id" : id,
		    "name" : name,
		    "category" : category,
		    "quantity" : quantity,
		    "price" : price
		}

		if quantity <= 0:
			return jsonify({"Message" : "You can not make a sale record with zero"})
		validate(new_sale, schema)

		# user_role = get_jwt_claims()
		
		# attendant = "attendant"

		# if user_role['role'] != attendant:
		# 	return jsonify({"message": "Only an attendant is permitted to post a sales record"}), 401
		sales.append(new_sale)
		
		return {"Message" : "Order added successfully", "Sales":sales}, 200


@api.route('/api/v1/sale/<int:id>')
class Sale(Resource):
	# @jwt_required
	def get(self, id):
		single_sale = [sale for sale in sales if sale['id'] == id]
		return {"order" : single_sale}, 200