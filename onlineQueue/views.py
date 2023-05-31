from django.shortcuts import render, get_object_or_404

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from onlineQueue.models import Queue
from onlineQueue.serializer import QueueSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class UserallOrder(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = Queue.objects.filter(user=request.user)
        if not queryset:
            return Response({'error': 'You dont have Queue'})
        else:
            serializers = QueueSerializer(queryset, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)



class QueueDetialView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Queue, id=pk)

    def get(self , request , *args , **kwargs):
        queryset = self.get_object(pk=self.kwargs.get('pk'))
        serializers = QueueSerializer(queryset)
        return Response(serializers.data)

    def delete(self, request, *args, **kwargs):
        queyset = self.get_object(pk=self.kwargs.get('pk'))
        queyset.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
