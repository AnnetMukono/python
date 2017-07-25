from django.db import models

# Create your models here.
class Student(models.Model):
    names = models.CharField(max_length= 200)
    course = models.TextField()
    year = models.IntegerField()
    
    def __str__(self):
        return self.names