from flask import Flask, jsonify, request, make_response
import jwt
import datetime
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({"Meassge" : "Token is missing."})

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return f(*args, **kwargs)

    return decorated