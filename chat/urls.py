from django.conf.urls import url

from chat import views

urlpatterns = [
                    url(r'^$', views.index1, name='index1'),
                    url(r'^(\d+)/$', views.chat_room, name='chat_room')
                       ]