from django.db import models

# Create your models here.

class green_table (models.Model):
    name = models.CharField(max_length=350)
    desc = models.TextField()
    date = models.DateField()
    img = models.ImageField(upload_to='pics')