from django.conf.urls import url
from mainapp import views as views
from twitterapp import views as twitterviews


urlpatterns = [
    #url(r'^$', twitterviews.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^details/$', views.user_details, name='details'),
    url(r'^invalid/$', views.invalid_entry, name='invalid'),
    #url(r'^simpleemail/(?P<emailto>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/',views.sendemail , name = 'sendSimpleEmail'),
    url(r'^contact/$', views.contact, name='contact'),
#neha-forgotpassword
    url(r'^forgotpassword/$', views.forgot_password, name='forgotpassword'),
    url(r'^invalidemail/$', views.invalid_email, name='invalidemail'),
    url(r'^resetpassword/$', views.reset_password, name='resetpassword'),
    url(r'^invalidusername/$', views.invalid_username, name='invalidusername'),
    url(r'^forgotusername/$', views.forgot_username, name='forgotusername'),
    url(r'^email/$', views.email, name='email'),
    url(r'^passwordchange/$', views.password_change, name='passwordchange'),
    ]

