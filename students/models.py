from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    cod = models.CharField(max_length=200)
    course = models.IntegerField()
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name