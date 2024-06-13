import unittest
from app import create_app, db
from app.models import User, WasteCollectionSchedule
from flask_login import login_user

class HouseholdTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            user = User(username='testuser', email='test@example.com', password='password', role='household')
            db.session.add(user)
            db.session.commit()
            login_user(user)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_schedule_waste_collection(self):
        response = self.client.post('/schedule', data=dict(
            schedule_date='2024-06-15'
        ))
        self.assertEqual(response.status_code, 302)
        self.assertIsNotNone(WasteCollectionSchedule.query.first())

if __name__ == '__main__':
    unittest.main()
