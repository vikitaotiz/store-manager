from flask import Blueprint, Flask, request
from flask_restplus import Api, Resource
from jsonschema import validate

from app.api.v1.models.models import orders
from app.api.v1.models.models import products
from app.api.v1.utils.validate import schema

from app.api.v1.views.products import app, api, token_required
api_orders = Blueprint('api_orders', __name__)
api_order = Blueprint('api_order', __name__)

@api.route('/api/v1/orders')
class Orders(Resource):
	def get(self):
		if len(orders) != 0 :
			return {"orders" : orders}, 200
		return {"Message":"There are no orders in stock."}
		
	@token_required	
	def post(self):
		req_data = request.get_json()
		id = len(orders) + 1
		name = req_data['name']
		category = req_data['category']
		quantity = req_data['quantity']
		price = req_data['price']

		product_name = [product for product in products if product['name'] == name]

		if not product_name:
			return "Product does not exist"
		product_name[0]["quantity"] = product_name[0]["quantity"] - 1
        
		new_order = {
		  "id" : id,
		    "name" : name,
		    "category" : category,
		    "quantity" : quantity,
		    "price" : price
		}
        
		validate(new_order, schema)
		orders.append(new_order)
		
		return {"Message" : "Order added successfully", "orders":orders}, 200


@api.route('/api/v1/order/<int:id>')
class Order(Resource):
	def get(self, id):
		single_order = [order for order in orders if order['id'] == id]
		return {"order" : single_order}, 200