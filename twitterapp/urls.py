from django.conf.urls import url
from twitterapp import views as views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    ]

