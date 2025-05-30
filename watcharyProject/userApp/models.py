from django.db import models

# Create your models here.
class User(models.Model):
    fullName = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.fullName