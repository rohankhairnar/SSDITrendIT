from django.conf.urls import url
from django_simple_forum import views as forumviews


urlpatterns = [
    url(r'^$', forumviews.index, name='forum-index'),
    url(r'^(\d+)/$', forumviews.forum, name='forum-detail'),
    url(r'^topic/(\d+)/$', forumviews.topic, name='topic-detail'),
    url(r'^reply/(\d+)/$', forumviews.post_reply, name='reply'),
    url(r'newtopic/(\d+)/$', forumviews.new_topic, name='new-topic'),
]