from django.urls import path
from .views import ProfileApiView, UserRegisterApiview

urlpatterns = [
    path('', ProfileApiView.as_view(), name='user_profile'),
    path('register/', UserRegisterApiview.as_view(), name='user_profile'),
]
