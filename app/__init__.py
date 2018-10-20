from flask import Blueprint

from app.api.v1.views.products import app, api_prods, api_prod

from app.api.v1.views.orders import app, api_orders, api_order

app.register_blueprint(api_prods)
app.register_blueprint(api_prod)
app.register_blueprint(api_orders)
app.register_blueprint(api_order)