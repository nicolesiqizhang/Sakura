from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_topics,  name='list_topics'),
    path('like/<int:topic_id>', views.like_topic, name='like_topic'),
    path('topic/<int:topic_id>', views.list_topic_threads)
]