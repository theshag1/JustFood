from django.urls import path

from .views import FoodAPIview, FoodDetilView, LikeDislikeApiview

urlpatterns = [
    path('', FoodAPIview.as_view(), name='food-view'),
    path('<int:pk>/likedislike/', LikeDislikeApiview.as_view(), name='like_or_dislike'),
    path('<slug:slug>', FoodDetilView.as_view(), name='food-detail-view'),
]
