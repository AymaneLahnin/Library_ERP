from django.db import models

# models.py
from neomodel import StructuredNode, StringProperty, IntegerProperty

class Person(StructuredNode):
    name = StringProperty(unique_index=True)
    age = IntegerProperty()
# Create your models here.
