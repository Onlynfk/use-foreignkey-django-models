from django.shortcuts import render



# Create your views here.
from django.views.generic import ListView, DetailView, View

from .models import ChildRecord, Immunize_schedule

class ChildRecordListView(ListView):
    model = ChildRecord


class ChildRecordDetailView(DetailView):
    model = ChildRecord

class ImmunizedScheduleView(View):
    def get(self, request, childrecord_slug, immunize_schedule_slug, *args, **kwargs):
        
        childrecord_qs = ChildRecord.objects.filter(slug=childrecord_slug)
        if childrecord_qs.exists():
            childrecord =  childrecord_qs.first()
        
        immunize_schedule_qs = childrecord.immunize_schedules.filter(slug=immunize_schedule_slug)
        if immunize_schedule_qs.exists():
            immunize_schedule = immunize_schedule_qs.first()

        context = {
            'object': immunize_schedule
        }
        
        return render(request, 'model_/immunize_list_detail.html', context )