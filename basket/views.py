from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Basket
from .serializers import BassketSerializer


# Create your views here.
class BasketApiView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Basket.objects.all()
    serializer_class = BassketSerializer

