"""定义learning_logs的URL模式"""
from django.conf.urls import url
from . import views

urlpatterns = [
    #homepage
    url(r'^$',views.index,name='index'),
    
    #display all topics
    url(r'^topics/$',views.topics,name='topics'),
    
    #specific topic's detailed webpage
    url(r'^topics/(?P<topic_id>\d+)$',views.topic,name='topic'),
]