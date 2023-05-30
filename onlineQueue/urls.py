from django.urls import path
from .views import QueueAPIview ,QueueDetialView

urlpatterns = [
    path('', QueueAPIview.as_view(), name='queue'),
    path('<int:pk>', QueueDetialView.as_view(), name='queue_detail')
]
