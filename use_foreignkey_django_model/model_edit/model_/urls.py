from django.urls import path
from model_.views import ChildRecordListView, ChildRecordDetailView,ImmunizedScheduleView

app_name = 'model_'

urlpatterns = [
    path('', ChildRecordListView.as_view(), name = 'list'),
    path('<slug>', ChildRecordDetailView.as_view(), name = 'detail'),
    
    path('<childrecord_slug>/<immunize_schedule_slug>', ImmunizedScheduleView.as_view(), name = 'immunize-detail'),
    


]