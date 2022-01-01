from django.db import models

# Create your models here.

class Forms(models.Model):
    name = models.TextField(max_length=100)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    category = models.CharField(max_length=15)