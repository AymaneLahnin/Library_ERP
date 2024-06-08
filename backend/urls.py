# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_person, name='create_person'),
    path('list/', views.list_persons, name='list_persons'),
]
