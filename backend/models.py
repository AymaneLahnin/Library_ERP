from django.db import models

# models.py
from neomodel import StructuredNode, StringProperty, IntegerProperty,RelationshipTo

class Person(StructuredNode):
    name = StringProperty(unique_index=True)
    age = IntegerProperty()
    job = RelationshipTo('Job', 'HAS_JOB')
    book = RelationshipTo('Book', 'HAS_BOOK')

class Job(StructuredNode):
    title = StringProperty(unique_index=True)
    salary = IntegerProperty()

class Book(StructuredNode):
    title = StringProperty(unique_index=True)
# Create your models here.
