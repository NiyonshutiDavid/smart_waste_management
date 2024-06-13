import unittest
from app import create_app, db
from app.models import User

class AuthTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_register(self):
        response = self.client.post('/register', data=dict(
            username='testuser',
            email='test@example.com',
            password='password'
        ))
        self.assertEqual(response.status_code, 302)

    def test_login(self):
        self.client.post('/register', data=dict(
            username='testuser',
            email='test@example.com',
            password='password'
        ))
        response = self.client.post('/login', data=dict(
            email='test@example.com',
            password='password'
        ))
        self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()
