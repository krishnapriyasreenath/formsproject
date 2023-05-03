from django.db import models
class employee(models.Model):
    empid=models.IntegerField()
    emp_name=models.CharField(max_length=75)
    emp_address=models.CharField(max_length=25)

# Create your models here.
