# from flask import Flask, jsonify, request, make_response
# import jwt
# import datetime
# from functools import wraps

# from app.api.v1.views.products import app

# app.config['SECRET_KEY'] = 'mysecret@12345'

# def token_required(f):
# 	@wraps(f)
# 	def decorated(*args, **kwargs):
# 		token = request.args.get('token')

# 		if not token:
# 			return jsonify({'message' : 'Token is missing!'})
# 		try:
# 			data = jwt.decode(token, app.config['SECRET_KEY'])
# 		except:
# 			return jsonify({'message' : 'Token is invalid'})

# 		return f(*args, **kwargs)

# 	return decorated
	

# @app.route('/login')
# def login():
# 	auth = request.authorization

# 	if auth and auth.password == "password":
# 		token = jwt.encode({"user" : auth.username, "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
# 		return jsonify({"token": token.decode("UTF-8")})

# 	return make_response('Could not verify', 401, {"WWW-Authenticate" : "Basic realm='Login Required'"})