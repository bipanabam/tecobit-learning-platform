from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # additional fields for our user model
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username