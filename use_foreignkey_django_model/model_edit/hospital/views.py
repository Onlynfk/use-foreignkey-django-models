from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Record, Schedule


class RecordListView(ListView):
    model = Record

class RecordDetailView(DetailView):
    model = Record
    
class ScheduleDetailView(View):
    def get(self, request, record_slug, schedule_slug, *args, **kwargs):
        record_qs = Record.objects.filter(slug=record_slug)
        if record_qs.exists():
            record = record_qs.first()

        schedule_qs = record.schedules.filter(slug=schedule_slug)
        if schedule_qs.exists():
            schedule = schedule_qs.first()
        
        context = {
            'object' : schedule
        }
        return render(request, "hospital/schedule_detail.html", context)
        