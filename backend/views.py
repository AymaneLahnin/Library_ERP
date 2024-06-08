from django.shortcuts import render

# views.py
from django.http import HttpResponse
from .models import Person,Job,Book

def create_person_and_job(request):
    # Create a job
    job = Job(title='Software Engineer', salary=120000).save()
    
    # Create a person
    person = Person(name='John Doe', age=30).save()

    book = Book(title='book1').save()
    
    # Create a relationship between person and job
    person.job.connect(job)

    person.book.connect(book)
    
    return HttpResponse(f'Created person: {person.name}, age: {person.age} with job: {job.title}, salary: {job.salary}')
def list_persons(request):
    persons = Person.nodes.all()
    persons_list = ', '.join([f'{p.name} (age {p.age})' for p in persons])
    return HttpResponse(f'Persons in database: {persons_list}')

# Create your views here.
