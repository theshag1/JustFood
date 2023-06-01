from django.urls import path

from .views import Paymethods

urlpatterns = [
    path('', Paymethods.as_view(), name='pay')
]
