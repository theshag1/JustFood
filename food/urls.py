from django.urls import path

from .views import FoodAPIview, FoodDetilView, LikeDislikeApiview, CommentView, CommentDetailView

urlpatterns = [
    path('', FoodAPIview.as_view(), name='food-view'),
    path('comment/', CommentView.as_view(), name='food-comment'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='food-comment-detil'),
    path('<int:pk>/like_dislike/', LikeDislikeApiview.as_view(), name='like_or_dislike'),
    path('<slug:slug>', FoodDetilView.as_view(), name='food-detail-view'),
]
