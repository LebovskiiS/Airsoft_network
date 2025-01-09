from unittest import TestCase
from app import app
from app.models import Event, Base, engine



class EventTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        cls.client = app.test_client()
        cls.client = app.test_client()
        cls.app = app



    def test_events_exists(self):
        response = self.client.get('/events')
        self.assertIn('events', response.get_data(as_text= True))



    def test_events_add(self):
        response = self.client.post('/events/add/submit',
                                   data= {'name':'test',
                                          'description':'test description'})
        self.assertIn('event submitted', response.get_data(as_text= True))





    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(engine)

