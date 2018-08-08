from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from . import views

urlpatterns=[
    url('^$', views.neighbourhood,name = 'home'),
    url(r'^new_neighbourhood/$', views.new_neighbourhood, name='new_neighbourhood'),
    url(r'^join/(\d+)',views.join_hood, name = 'join_hood'),
    url(r'^exithood/(\d+)',views.exithood,name = 'exithood'),
    url(r'^create_business/$', views.create_business, name='create_business'),
    url(r'^create_allert/$', views.post_allert, name='create_allert'),
    url(r'^create_comment/(?P<post_id>\d+)', views.create_comment, name='create_comment'),
]
