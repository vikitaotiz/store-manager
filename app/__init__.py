from flask import Blueprint

from app.api.v1.views.products import app, api_prods, api_prod
from app.api.v1.views.sales import app, api_sales, api_sale
# from app.api.v1.views.auth_api import register, login, user_username, logout, all_users

app.register_blueprint(api_prods)
app.register_blueprint(api_prod)
app.register_blueprint(api_sales)
app.register_blueprint(api_sale)

# app.register_blueprint(register)
# app.register_blueprint(login)
# app.register_blueprint(user_username)
# app.register_blueprint(logout)
# app.register_blueprint(all_users)