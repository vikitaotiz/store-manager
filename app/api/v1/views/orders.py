from flask import Blueprint, Flask, request
from flask_restplus import Api, Resource
import jwt
import datetime
from functools import wraps

from app.api.v1.utils import token_required
from app.api.v1.models import orders

from app.api.v1.views.products import app, api, login

api_orders = Blueprint('api_orders', __name__)
api_order = Blueprint('api_order', __name__)
app.config['SECRET_KEY'] = "mysecretkey@9812"


@api.route('/orders')
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

		new_order = {
		  "id" : id,
		  "desc" : {
		    "name" : name,
		    "category" : category,
		    "quantity" : quantity,
		    "price" : float(price)
		  }
		}

		orders.append(new_order)

		return {"Message" : "Order added successfully", "orders":orders}, 200


@api.route('/order/<int:id>')
class Order(Resource):
	def get(self, id):
		single_order = [order for order in orders if order['id'] == id]
		return {"order" : single_order}, 200