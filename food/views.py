from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Food, LikeDislike
from .serializer import FoodSerializer, LikeDislikeSerializer


# Create your views here.


class FoodAPIview(APIView):
    def get(self, request):
        queryset = Food.objects.order_by('-id')
        serializer = FoodSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class FoodDetilView(generics.RetrieveUpdateDestroyAPIView):
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
