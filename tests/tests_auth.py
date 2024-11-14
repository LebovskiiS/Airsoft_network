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




