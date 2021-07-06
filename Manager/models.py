from django.db import models

# Create your models here.
class Credentials(models.Model):
    added_date = models.DateTimeField()
    Site_Name = models.CharField(max_length=200)
    UID = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)

        
