from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass



class Book(models.Model):
    name = models.CharField(max_length=25)
    author = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



