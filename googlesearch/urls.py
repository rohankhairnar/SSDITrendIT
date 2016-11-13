from django.conf.urls import url
from django.views.generic.base import TemplateView
from googlesearch import views


urlpatterns = [
    url(r'^results/$',TemplateView.as_view(template_name='googlesearch/results.html'),name='googlesearch_results'),

    url(r'^cref-cse\.xml/$',views.cref_cse,{},name='googlesearch-cref-cse'),
]
