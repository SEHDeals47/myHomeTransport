from django.db import models

# Create your models here.
class Harare_Students(models.Model):
    seat_number =  models.CharField(max_length=10)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    registration_number = models.CharField(max_length=120)
    
    def __str__(self):
        return self.last_name 

class Marondera_Students(models.Model):
    seat_number =  models.CharField(max_length=10)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    registration_number = models.CharField(max_length=120)
    
    def __str__(self):
        return self.last_name 

