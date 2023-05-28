from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from Category.models import Category
from .serializer import CategorySerialzer


# Create your views here.

class CategoryAPIView(APIView):
    def get(self, request):
        queryset = Category.objects.order_by('-position')
        serializer = CategorySerialzer(queryset, many=True)
        return Response(serializer.data)


class CategoryDetailAPiview(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerialzer
    lookup_field = 'slug'
