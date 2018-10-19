from flask import Blueprint, Flask, request, make_response, jsonify
from flask_restplus import Api, Resource
import jwt
import datetime
from functools import wraps

from app.api.v1.utils import token_required
from app.api.v1.models import products

authorizations = {
        'apiKey' : {
            'type' : 'apiKey',
            'in' : 'header',
            'name' : 'X-API-KEY'
        }
    }

app = Flask(__name__)
api = Api(app, authorizations=authorizations)

api_prods = Blueprint('api_prods', __name__)
api_prod = Blueprint('api_prod', __name__)

app.config['SECRET_KEY'] = "mysecretkey@9812"

@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == 'password':
        token = jwt.encode({"user" : auth.username, "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes = 30)}, app.config['SECRET_KEY'])
        return jsonify({"Token": token.decode('UTF-8')})
    return make_response('Could not verify', 401, {'WWW-Authorization' : "Basic realm="login required"'})


@api.route('/products')
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
		  "desc" : {
		    "name" : name,
		    "category" : category,
		    "quantity" : quantity,
		    "price" : float(price)
		  }
		}

		products.append(new_product)

		return {"Message" : "Product added successfully", "Products":products}, 200


@api.route('/product/<int:id>')
class Product(Resource):
	def get(self, id):
		single_product = [product for product in products if product['id'] == id]
		return {"Product" : single_product}, 200