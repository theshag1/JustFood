from django.urls import path
from .views import UserallOrder, QueueDetialView

urlpatterns = [
    path('', UserallOrder.as_view(), name='queue'),
    path('<int:pk>', QueueDetialView.as_view(), name='queue_detail')
]
