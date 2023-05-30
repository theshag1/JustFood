from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from onlineQueue.models import Queue
from onlineQueue.serializer import QueueSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class QueueAPIview(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = Queue.objects.filter(user=request.user)
        if not queryset:
            return Response({'error': 'You dont have Queue'})
        else:
            serializers = QueueSerializer(queryset, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializers = QueueSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
