"""trenditapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from mainapp import urls
from django.views.generic import RedirectView
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('mainapp.urls')),
    url(r'^', include('twitterapp.urls')),
<<<<<<< HEAD
=======
    url(r'^chats/', include('chat.urls')),
    url(r'^(/)?$', RedirectView.as_view(url='/chats/')),
>>>>>>> master
    url(r'^search/', include('googlesearch.urls')),
    url(r'^forum/', include('django_simple_forum.urls')),
]
