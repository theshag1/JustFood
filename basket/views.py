from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Basket
from .serializers import BasketSerializer


# Create your views here.


class BasketApiView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
