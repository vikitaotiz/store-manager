import unittest
import json
import jwt

from instance.config import app_config
from app.api.v1.views.orders import Orders
from app import app

class TestOrders(unittest.TestCase):
    def setUp(self):
        self.tests = app.test_client()
        self.tests.testing = True

        order_info = json.dumps({
        "name" : "Woofer",
        "category" : "Electronics",
        "quantity" : 3,
        "price" : 600
        })

        self.create_order = self.tests.post('/orders', data = order_info, content_type="application/json")
   
    def tearDown(self):
        self.tests = None

    def test_get_orders(self):
        result = self.tests.get("/orders", content_type="application/json")
        self.assertEqual(result.status_code, 200)

    def test_post_orders(self):
        order_data = json.dumps({
            "name" : "Woofer",
            "category" : "Electronics",
            "quantity" : 3,
            "price" : 600
        })

        res = self.tests.post('/orders', data = order_data, content_type="application/json")
        self.assertEqual(res.status_code, 200)

    def test_get_order(self, id):
        result = self.tests.get("/order/1", content_type="application/json")
        self.assertEqual(result.status_code, 200)