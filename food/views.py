from django.http import Http404
from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Food, LikeDislike, Comment
from .serializer import FoodSerializer, LikeDislikeSerializer, CommentSerializer


# Create your views here.


class FoodAPIview(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Food.objects.order_by()
        serializer = FoodSerializer(queryset, many=True)
        return Response(serializer.data)


class FoodDetilView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Food.objects.all()
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return FoodSerializer
        return FoodSerializer


class LikeDislikeApiview(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=LikeDislikeSerializer)
    def post(self, request, *args, **kwargs):
        serializer = LikeDislikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        types = serializer.validated_data.get('type')
        user = request.user
        food = Food.objects.filter(id=self.kwargs.get('pk')).first()
        if not food:
            raise Http404
        like_dislike = LikeDislike.objects.filter(food=food, user=user).first()
        if like_dislike and like_dislike == types:
            like_dislike.delete()
        else:
            LikeDislike.objects.update_or_create(food=food, user=user, defaults={'type': types})
            data = {'type': types, 'detail': 'liked_or disliked'}
        return Response(data)


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
