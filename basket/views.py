from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Basket
from .serializers import BasketSerializer


# Create your views here.


class BasketApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = Basket.objects.all()
        serializer = BasketSerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        serializer = BasketSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            amount = serializer.validated_data
            print(amount)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
