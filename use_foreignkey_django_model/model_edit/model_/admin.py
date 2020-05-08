from django.contrib import admin

# Register your models here.
from .models import ChildRecord, Immunize_schedule

admin.site.register(ChildRecord)
admin.site.register(Immunize_schedule)
