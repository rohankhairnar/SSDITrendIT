from django.test import TestCase
from mainapp.models import UserProfile
from unittest import TestCase
from django.db import models
from mainapp.forms import *
from django.test import Client
from mainapp import views
from django.core.urlresolvers import reverse

from mainapp.forms import UserForm, UserProfileForm
from django.template import RequestContext

from django.shortcuts import render, render_to_response
from mainapp.models import UserProfile, User
from mainapp.forms import UserForm, UserProfileForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


class TestRegister(TestCase):
    def test_register(self):
        self.client = Client()
        self.user = User.objects.create_user('rohankhairnar12131','rohan1212@gmail.com', 'abcdefg')
        self.assertEquals(self.user.email, 'rohan1212@gmail.com')

    #def test_register2(self):
     #   self.client = Client()
      #  self.user = User.objects.create_user('rohankhairnar', 'rohan@gmail.com', 'abcdefg')
        #self.assertEquals(authenticate(self.user.username), 'rohankhairnar')
        #UserProfile.objects.create(User)


