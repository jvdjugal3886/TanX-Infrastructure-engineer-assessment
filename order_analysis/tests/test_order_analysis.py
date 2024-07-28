import unittest
import pandas as pd  # Add this import
from main import compute_total_revenue_by_month, compute_total_revenue_by_product, compute_total_revenue_by_customer, get_top_10_customers, read_data

class TestOrderAnalysis(unittest.TestCase):

    def setUp(self):
        # Sample data to use in tests
        self.data = [
            {"order_id": 1, "customer_id": 1, "order_date": "2023-01-01", "product_id": 101, "product_name": "Product A", "product_price": 10.0, "quantity": 2},
            {"order_id": 2, "customer_id": 1, "order_date": "2023-01-05", "product_id": 102, "product_name": "Product B", "product_price": 20.0, "quantity": 1},
            {"order_id": 3, "customer_id": 2, "order_date": "2023-02-01", "product_id": 101, "product_name": "Product A", "product_price": 10.0, "quantity": 3},
            {"order_id": 4, "customer_id": 3, "order_date": "2023-02-10", "product_id": 103, "product_name": "Product C", "product_price": 30.0, "quantity": 1},
            {"order_id": 5, "customer_id": 1, "order_date": "2023-03-15", "product_id": 104, "product_name": "Product D", "product_price": 25.0, "quantity": 2},
            {"order_id": 6, "customer_id": 2, "order_date": "2023-03-20", "product_id": 105, "product_name": "Product E", "product_price": 15.0, "quantity": 5},
            {"order_id": 7, "customer_id": 4, "order_date": "2023-04-05", "product_id": 106, "product_name": "Product F", "product_price": 40.0, "quantity": 1},
            {"order_id": 8, "customer_id": 3, "order_date": "2023-04-12", "product_id": 101, "product_name": "Product A", "product_price": 10.0, "quantity": 1},
            {"order_id": 9, "customer_id": 5, "order_date": "2023-05-01", "product_id": 103, "product_name": "Product C", "product_price": 30.0, "quantity": 2},
            {"order_id": 10, "customer_id": 6, "order_date": "2023-05-20", "product_id": 107, "product_name": "Product G", "product_price": 50.0, "quantity": 1},
        ]

    def test_compute_total_revenue_by_month(self):
        df = pd.DataFrame(self.data)
        result = compute_total_revenue_by_month(df)
        expected = {
            '2023-01': 40.0,
            '2023-02': 60.0,
            '2023-03': 125.0,
            '2023-04': 50.0,
            '2023-05': 110.0
        }
        self.assertEqual(result, expected)

    def test_compute_total_revenue_by_product(self):
        df = pd.DataFrame(self.data)
        result = compute_total_revenue_by_product(df)
        expected = {
            'Product A': 60.0,
            'Product B': 20.0,
            'Product C': 90.0,
            'Product D': 50.0,
            'Product E': 75.0,
            'Product F': 40.0,
            'Product G': 50.0
        }
        self.assertEqual(result, expected)

    def test_compute_total_revenue_by_customer(self):
        df = pd.DataFrame(self.data)
        result = compute_total_revenue_by_customer(df)
        expected = {
            1: 90.0,
            2: 105.0,
            3: 40.0,
            4: 40.0,
            5: 60.0,
            6: 50.0
        }
        self.assertEqual(result, expected)

    def test_get_top_10_customers(self):
        revenue_by_customer = {
            1: 90.0,
            2: 105.0,
            3: 40.0,
            4: 40.0,
            5: 60.0,
            6: 50.0
        }
        result = get_top_10_customers(revenue_by_customer)
        expected = [
            (2, 105.0),
            (1, 90.0),
            (5, 60.0),
            (6, 50.0),
            (3, 40.0),
            (4, 40.0)
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
