# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_person_and_job, name='create_person_and_job'),
    path('list/', views.list_persons, name='list_persons'),
]
