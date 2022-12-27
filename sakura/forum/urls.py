from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_topics),
    path('topic/<int:topic_id>', views.list_threads)
]