from django.test import TestCase
from django.test import Client
from django.db import models
from django.contrib.auth.models import User
from mainapp.forms import UserForm
#from mainapp.views import user_login
import nose.tools as nt
#from django.core.urlresolvers import reverse

class TestRegister(TestCase):
    def test_register(self):
        self.client = Client()
        self.user = User.objects.create_user('rohankhairnar12131','rohan1212@gmail.com', 'abcdefg')
        self.assertEquals(self.user.email, 'rohan1212@gmail.com')

    def test_register2(self):
        self.client = Client()
        self.user = User.objects.create_user('rohankhairnar', 'rohan@gmail.com', 'abcdefg')
        #self.username=self.User.get(username=self.user.username)
        self.assertEquals((self.user.username), 'rohankhairnar')
        #UserProfile.objects.create(User)

    def test_user_form(self):
        form_data = {'fullname':'Aarti Pathak','username': 'aartipathak', "email":"rtpathak@gmail.com", "password1":"asdf", "password2": "asdf",}
        form = UserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_login(self):
         #self.client.login(username='rohankhairnar',password='khairnar')
         response=self.client.post('/login',{'username':'rohankhairnar','password':'khairnar'})
         if(response.content.find("Welcome to Trend!t")==1):
             nt.assert_true