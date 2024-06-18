import unittest
from app import app, db
from app.models import User

class BasicTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        response = self.app.post('/register', data=dict(
            username='testuser',
            email='test@test.com',
            password='password',
            confirm='password'
        ), follow_redirects=True)
        self.assertIn(b'Login', response.data)

if __name__ == "__main__":
    unittest.main()
