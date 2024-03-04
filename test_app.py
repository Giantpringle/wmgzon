import unittest
from app import app, db, Product

class ProductTestCase(unittest.TestCase):
    def setUp(self):
        # Push an application context
        self.app_context = app.app_context()
        self.app_context.push()

        # Configure the app for testing
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = app.test_client()

        # Create the database and tables
        db.create_all()

    def tearDown(self):
        # Drop all the data after each test
        db.session.remove()
        db.drop_all()

        # Pop the application context
        self.app_context.pop()

    def test_add_product(self):
        # Test adding a product
        response = self.client.post('/add_product', json={
            'name': 'Tennis Racket',
            'description': 'High quality tennis racket',
            'price': 150.00,
            'category': 'Sports',
            'image': 'tennis_racket.jpg'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Product added successfully', response.get_json()['message'])

    def test_search_product(self):
        # Setup: Add a product to search for
        self.client.post('/add_product', json={
            'name': 'Tennis Racket',
            'description': 'High quality tennis racket',
            'price': 150.00,
            'category': 'Sports',
            'image': 'tennis_racket.jpg'
        })

        # Execute: Search for the product
        response = self.client.get('/products?search=Tennis')
        self.assertEqual(response.status_code, 200)

        # Validate: Check if the product is in the search results
        data = response.get_json()
        self.assertTrue(any('Tennis Racket' in product['name'] for product in data))

if __name__ == '__main__':
    unittest.main()
