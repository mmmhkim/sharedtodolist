from unittest.util import _MAX_LENGTH
from django.db import models
from django.db import connections
from django.contrib.auth.models import User

class Item(models.Model):
    content = models.TextField()
