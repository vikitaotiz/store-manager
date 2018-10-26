import unittest
import json

from app.api.v1.views.sales import Sales, Sale
from app import app

class TestSales(unittest.TestCase):
    def setUp(self):
        self.tests = app.test_client()
        self.tests.testing = True

        sale_info = json.dumps({
        "name" : "Woofer",
        "category" : "Electronics",
        "quantity" : 3,
        "price" : 600
        })

        self.sale_error = json.dumps({
        "name" : "",
        "category" : "Electronics",
        "quantity" : 3,
        "price" : 600
        })

        self.create_order = self.tests.post('/api/v1/sales', data = sale_info, content_type="application/json")
   
    def tearDown(self):
        self.tests = None

    def test_get_sales(self):
        result = self.tests.get("/api/v1/sales", content_type="application/json")
        self.assertEqual(result.status_code, 200)

    def test_post_sales(self):
        sale_data = json.dumps({
            "name" : "Woofer",
            "category" : "Electronics",
            "quantity" : 3,
            "price" : 600
        })

        res = self.tests.post('/api/v1/sales', data = sale_data, content_type="application/json")
        self.assertEqual(res.status_code, 200)

    def test_get_sale(self):
        result = self.tests.get("/api/v1/sale/1", content_type="application/json")
        self.assertEqual(result.status_code, 200)

    def test_invalid_data(self):
        res = self.tests.post('/api/v1/sales', data = self.sale_error, content_type="application/json")
        self.assertEqual(res.status_code, 200)