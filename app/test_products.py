import unittest
import json

from app.api.v1.views.products import Products, Product
from app import app

class TestProducts(unittest.TestCase):
    def setUp(self):
        self.tests = app.test_client()
        self.tests.testing = True

        product_info = json.dumps({
        "name" : "Woofer",
        "category" : "Electronics",
        "quantity" : 3,
        "price" : 600
        })

        self.create_product = self.tests.post('/api/v1/products', data = product_info, content_type="application/json")
   
    def tearDown(self):
        self.tests = None

    def test_get_products(self):
        result = self.tests.get("/api/v1/products", content_type="application/json")
        self.assertEqual(result.status_code, 200)

    def test_post_products(self):
        order_data = json.dumps({
            "name" : "Woofer",
            "category" : "Electronics",
            "quantity" : 3,
            "price" : 600
        })

        res = self.tests.post('/api/v1/products', data = order_data, content_type="application/json")
        self.assertEqual(res.status_code, 200)
        
    def test_get_product(self):
        result = self.tests.get("/api/v1/product/1", content_type="application/json")
        self.assertEqual(result.status_code, 200)