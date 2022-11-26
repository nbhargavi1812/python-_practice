from django.db import models

# Create your models here.
class student(models.Model):
    student_id=models.IntegerField()
    student_name=models.CharField(max_length=20)
    student_mobileno=models.CharField(max_length=20)
