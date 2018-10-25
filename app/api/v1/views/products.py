from flask import Flask, request, Blueprint, make_response, jsonify
from flask_restplus import Resource, Api
from jsonschema import validate
import jwt
import datetime
from functools import wraps

from app.api.v1.models.models import products
from app.api.v1.utils.validate import schema

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'mysecret@12345'

api_prods = Blueprint('api_prods', __name__)
api_prod = Blueprint('api_prod', __name__)

def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = request.args.get('token')

		if not token:
			return jsonify({'message' : 'Token is missing!'})
		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])
		except:
			return jsonify({'message' : 'Token is invalid'})

		return f(*args, **kwargs)

	return decorated

@api.route('/api/v1/products')
class Products(Resource):
	def get(self):
		if len(products) != 0 :
			return {"Products" : products}, 200
		return {"Message":"There are no products in stock."}

	@token_required
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

		validate(new_product, schema)
		products.append(new_product)

		return {"Message" : "Product added successfully", "Products":products}, 200


@api.route('/api/v1/product/<int:id>')
class Product(Resource):
	def get(self, id):
		single_product = [product for product in products if product['id'] == id]
		return {"Product" : single_product}, 200
	

@api.route('/api/v1/login')
class Login(Resource):
	def post(self):
		auth = request.authorization

		if auth and auth.password == "password":
			token = jwt.encode({"user" : auth.username, "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
			return jsonify({"token": token.decode("UTF-8")})

		return make_response('Could not verify', 401, {"WWW-Authenticate" : "Basic realm='Login Required'"})
