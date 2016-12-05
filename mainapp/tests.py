from django.test import TestCase
from django.test import Client
#from django.db import models
from django.contrib.auth.models import User
from mainapp.forms import UserForm
from mainapp.forms import ContactForm,ResetPasswordForm
#from mainapp.views import user_login
import nose.tools as nt
from django.core.urlresolvers import reverse
from django.core import mail
from django.test import TestCase

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

    #def test_login(self):
         #self.client.login(username='rohankhairnar',password='khairnar')
         #response=self.client.post('/login',{'username':'rohankhairnar','password':'khairnar'})
         #if(response.content.find("Welcome to Trend!t")==1):
             #nt.assert_true

    def test_accountdetails(self):
        self.client=Client()
        response=self.client.get('/details/')
        self.assertEqual(response.status_code,200)


    def test_contact_form_invaid(self):
        form_data = {'contact_name':'Aarti Pathak',"contact_email":"rtpathak", "contact_subject":"login issue", "contact_message": "Hi Team",}
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_contact_form(self):
        form_data = {'contact_name':'Aarti Pathak',"contact_email":"rtpathak@gmail.com", "contact_subject":"login issue", "contact_message": "Hi Team",}
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())


    def test_reset_password_form(self):
        form_data = {'username':'ndalvi1',"password":"asdf123", "password2":"asdf123"}
        form = ResetPasswordForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_url(self):
        self.client = Client()
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)



    def test_forgot_password_url(self):
        self.client = Client()
        response = self.client.get('/forgotpassword/')
        self.assertEqual(response.status_code, 200)

    def test_forgot_username_url(self):
        self.client = Client()
        response = self.client.get('/forgotusername/')
        self.assertEqual(response.status_code, 200)

    def test_login_url(self):
        self.client=Client()
        response=self.client.get('/login/')
        self.assertEqual(response.status_code,200)

    # with self.assertTemplateUsed('index.html'):
    #     render_to_string('index.html')
    # with self.assertTemplateUsed(template_name='index.html'):
    #     render_to_string('index.html')

    def test_send_email(self):
        # Send message.
        mail.send_mail(
            'Subject here', 'Here is the message.',
            'from@example.com', ['to@example.com'],
            fail_silently=False,
        )
        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

