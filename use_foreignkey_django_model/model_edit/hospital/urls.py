
from django.urls import path
from .views import RecordListView, RecordDetailView, ScheduleDetailView

app_name = 'hospital'


urlpatterns = [
    
    path('',RecordListView.as_view(), name='list' ),
    path('<slug>', RecordDetailView.as_view(), name="detail"),
    path('<record_slug>/<schedule_slug>/', ScheduleDetailView.as_view(), name="record-detail"),
    

]


