import random
import re
from flask import Flask, request, jsonify, Blueprint, make_response
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_raw_jwt
from app.api.v1.models.auth import Users
from app.api.v1.utils.utils import iterate_list
from app.api.v1.views.products import app, api
# api = Blueprint('api', __name__)

unapiorized = set()
user_obj = Users()


@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Fields cannot be empty"}), 400
    username = data.get('username').strip()
    name = data.get('name')
    email = data.get('email').strip()
    password = data.get('password').strip()
    confirm_password = data.get('confirm_password').strip()
    role = data.get('role').lower().strip()
    roles = ["admin", "attendant"]
    if role not in roles:
        return jsonify({"message": "The role {} does not exist.Only admin and attendant roles are allowed".format(role)}), 400

    userinfo = [username, name, role, password, confirm_password, email]

    exists = iterate_list(userinfo)
    if exists is False:
        return jsonify({"message": "Make sure all fields have been filled out"}), 206
    if len(password) < 4:
        return jsonify({"message": "The password is too short,minimum length is 4"}), 400
    if confirm_password != password:
        return jsonify({"message": "The passwords you entered don't match"}), 400
    match = re.match(
        r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    if match is None:
        return jsonify({"message": "Enter a valid email address"}), 403
    response = jsonify(user_obj.put(name, username, email, password, role))
    response.status_code = 201
    return response


@api.route('/login', methods=['POST'])
def login():
    '''login user by verifying password and creating an access token'''
    data = request.get_json()
    if not data:
        return jsonify({"message": "Fields cannot be empty"}), 400
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"message": "Username or password missing"}), 206
    apiorize = user_obj.verify_password(username, password)
    user = user_obj.user_username(username)
    if apiorize == "True":
        access_token = create_access_token(identity=user)
        return jsonify(dict(token=access_token, message="Login successful!")), 200

    response = jsonify(apiorize)
    response.status_code = 401
    return response


@api.route('/logout', methods=['POST'])
@jwt_required
def logout():
    json_token_identifier = get_raw_jwt()['jti']
    unapiorized.add(json_token_identifier)
    return jsonify({"message": "Successfully logged out"}), 200


@api.route('/users', methods=['GET'])
def all_users():
    response = make_response(jsonify(user_obj.all_users()))
    response.status_code = 200
    return response


@api.route('/users/<username>', methods=['GET'])
def user_username(username):
    response = make_response(
        jsonify(user_obj.user_username(username)))
    response.status_code = 200
    return response