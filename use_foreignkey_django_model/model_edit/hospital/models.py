from django.db import models
from  django.urls import reverse
# Create your models here.
class Record(models.Model):
    slug = models.SlugField()
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    birth_date = models.DateTimeField()
    weight = models.CharField(max_length=10)
    height = models.CharField(max_length=10)
    parent_name = models.CharField(max_length=200)
    parent_mobile = models.CharField(max_length=16)
    home_address = models.CharField(max_length=300)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    def get_absolute_url(self):
        return reverse("hospital:detail", kwargs={"slug": self.slug})
    
    @property
    def schedules(self):
        return self.schedule_set.all().order_by('position')

    
    
class Schedule(models.Model):
    slug = models.SlugField()
    date_immunized =  models.DateTimeField()
    initial_date = models.DateTimeField()
    record = models.ForeignKey(Record, on_delete = models.SET_NULL, null =True)
    disease_type = models.CharField(max_length = 30)
    vaccine_type = models.CharField(max_length=30)
    position = models.IntegerField()
    
    def __str__(self):
        return self.vaccine_type + " for " + self.disease_type 
    
    def get_absolute_url(self):
        return reverse("hospital:record-detail", kwargs={
            
            'record_slug': self.record.slug,
            'schedule_slug':self.slug,
            
            
            })
    
    
    
    
    
    