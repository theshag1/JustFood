from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser

from Category.models import Category
from .serializer import CategorySerialzer


# Create your views here.

class CategoryAPIView(APIView):
    def get(self, request):
        queryset = Category.objects.order_by('-position')
        serializer = CategorySerialzer(queryset, many=True)
        return Response(serializer.data)

    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializers = CategorySerialzer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAPiview(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerialzer
    lookup_field = 'slug'
