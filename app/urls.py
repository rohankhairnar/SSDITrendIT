from django.conf.urls import url
from app import views as views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^details/$', views.user_details, name='details'),
    url(r'^invalid/$', views.invalid_entry, name='invalid'),
    ]