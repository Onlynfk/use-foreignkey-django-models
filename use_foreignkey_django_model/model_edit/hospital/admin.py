from django.contrib import admin

# Register your models here.
from .models import Record, Schedule

admin.site.register(Record)
admin.site.register(Schedule)