import unittest
from app import create_app, db
from app.models import User, WasteCollectionSchedule

class ServicesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            user = User(username='serviceuser', email='service@example.com', password='password', role='service')
            db.session.add(user)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_view_schedules(self):
        schedule = WasteCollectionSchedule(user_id=1, schedule_date='2024-06-15')
        db.session.add(schedule)
        db.session.commit()
        response = self.client.get('/services')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
