import unittest
from app import create_app, db
from app.models import User, WasteCollectionSchedule, RecyclingTracker

class AdminTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            user = User(username='adminuser', email='admin@example.com', password='password', role='admin')
            db.session.add(user)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_view_admin_dashboard(self):
        response = self.client.get('/admin')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
