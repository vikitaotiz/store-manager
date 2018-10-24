from flask import Flask, jsonify, request, make_response
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = "mysecretkey@9812"

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

@app.route('/unprotected')
def unprotected():
    return "Hello there"

@app.route('/protected')
@token_required
def  protected():
    return {"Meassge" : "Private data"}

@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == 'password':
        token = jwt.encode({"user" : auth.username, "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes = 30)}, app.config['SECRET_KEY'])
        return jsonify({"Token": token.decode('UTF-8')})
    return make_response('Could not verify', 401, {"WWW-Authorization" : "Basic login required"})


if __name__ == '__main__':
    app.run(debug=True)