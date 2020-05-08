from django.db import models

# Create your models here.
class ChildRecord(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    birth_date = models.DateTimeField()
    parent_name = models.CharField(max_length=200)
    parent_mobile = models.CharField(max_length=16)
    home_address = models.CharField(max_length=300)
    hospital_at_birth = models.CharField(max_length=300)
    
    def __str__(self):
        return self.first_name + " " + self.last_name




    
    
    
    
    