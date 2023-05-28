from django.urls import path
from .views import CategoryAPIView, CategoryDetailAPiview

urlpatterns = [
    path('', CategoryAPIView.as_view(), name='category_view'),
    path('<slug:slug>', CategoryDetailAPiview.as_view(), name='category_detil_view'),
]
