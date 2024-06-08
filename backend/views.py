from django.shortcuts import render

# views.py
from django.http import HttpResponse
from .models import Person

def create_person(request):
    person = Person(name='John Doe', age=30).save()
    return HttpResponse(f'Created person: {person.name}, age: {person.age}')

def list_persons(request):
    persons = Person.nodes.all()
    persons_list = ', '.join([f'{p.name} (age {p.age})' for p in persons])
    return HttpResponse(f'Persons in database: {persons_list}')

# Create your views here.
