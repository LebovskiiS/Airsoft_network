from http.client import responses
from unittest import TestCase
from app import app
from app.models import User, Base, engine

class AuthTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        cls.client = app.test_client()
        cls.client = app.test_client()
        cls.app = app



    def test_login_page_exists(self):
        response = self.client.get('/auth/login')
        self.assertEqual(200, response.status_code)
        self.assertIn('Login', response.get_data(as_text= True))



    def test_registration_page_exists(self):
        response = self.client.get('/auth/registration')
        self.assertEqual(200, response.status_code)
        self.assertIn('Registration',response.get_data(as_text= True))



    def test_registration_user_added_to_db(self):
        test_data = {'email':'test_test61s@gmail.com', 'password':'e6rfdsdf','username':'testsfr1om6tests' }
        response = self.client.post('/auth/registration/submit', data= test_data)
        self.assertEqual('submitted', response.get_data(as_text=True))



    def test_same_data_registration(self):
        test_data = {'email': 'tes4t1@gmail.com', 'password': 'test31', 'username': 'test3t1'}
        response = self.client.post('/auth/registration/submit', data=test_data)
        self.assertEqual('submitted', response.get_data(as_text=True))
        response = self.client.post('/auth/registration/submit', data=test_data)
        self.assertEqual('error not uniq data entered', response.get_data(as_text= True))


    def test_empty_fields_registration(self):
        test_data = {'email': '', 'password': '', 'username': ''}
        response = self.client.post('/auth/registration/submit', data = test_data)
        self.assertEqual('error, fill up required fields', response.get_data(as_text= True))




    def test_login_submit(self):
        test_data = {'email': 'ttest@gmail.com', 'password': 'testpassword', 'username': 'testt1'}
        self.client.post('/auth/registration/submit', data=test_data)
        response = self.client.post('/auth/login/submit', data= {'email': 'test@gmail.com',
                                                       'password':'testpassword'}                          )
        self.assertEqual(200, response.status_code)




    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(engine)
