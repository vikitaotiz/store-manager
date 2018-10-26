# import string
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.api.v1.utils.utils import item_key, get_all

users = []

class Users():
    def put(self, name, username, email, password, role):
        self.user_dict = {}
        email_data = item_key("email", email, users)
        username_data = item_key("username", username, users)
        if "message" not in email_data:
            return {"message": "Email already in use,try a different one!"}
        if "message" not in username_data:
            return {"message": "Username already taken, try a different one"}

        self.user_dict["name"] = name
        self.user_dict["email"] = email
        self.user_dict["username"] = username
        self.user_dict["role"] = role
        pw_hash = generate_password_hash(password)
        self.user_dict["password"] = pw_hash

        users.append(self.user_dict)
        return {"message": "User with username {} added successfully".format(username)}

    def verify_password(self, username, password):
        user_obj = item_key('username', username, users)
        if "message" not in user_obj:
            result = check_password_hash(
                user_obj['password'], password)
            if result is True:
                return "True"
            return {"message": "The password you entered is incorrect"}
        return user_obj

    def user_username(self, username):
        result = item_key('username', username, users)
        return result

    def all_users(self):
        result = get_all(users)
        return result
