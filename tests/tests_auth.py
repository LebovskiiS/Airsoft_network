from http.client import responses
from unittest import TestCase

from flask import request

from app import app



class AuthTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        cls.client = app.test_client()


    def test_login_page_exists(self):
        response = self.client.get('/auth/login')
        self.assertEqual(200, response.status_code)
        self.assertIn('Login', response.get_data(as_text= True))


    def test_registration_page_exists(self):
        response = self.client.get('/auth/registration')
        self.assertEqual(200, response.status_code)
        self.assertIn('Registration',response.get_data(as_text= True))


    def test_login_submit(self):

        response = self.client.post('/auth/login/submit', data= {'email': 'test@gmail.com',
                                                                'password':'testpassword'}
                                   )
        self.assertEqual(200, response.status_code)




    def test_registration_submit(self):
        response = self.client.post('/auth/registration/submit', data= {'username':'test',
                                                                       'email':'test@test.com',
                                                                       'password':'testpass'}
        )
        self.assertEqual(200, response.status_code)


