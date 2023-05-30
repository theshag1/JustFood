from django.urls import path
from .views import QueueAPIview

urlpatterns = [
    path('', QueueAPIview.as_view(), name='queue')
]
