from django.urls import path

from .views import BasketApiView

urlpatterns = [
    path('', BasketApiView.as_view(), name='basket-view')
]
