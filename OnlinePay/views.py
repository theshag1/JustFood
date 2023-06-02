from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import PayMethod
from .serializer import OnlinePaySerializer, PaySerializer
import datetime


# Create your views here.

class Paymethods(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = PayMethod.objects.filter(user=request.user)
        serializer = OnlinePaySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = PaySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        balance = PayMethod.objects.get(user=request.user).balance
        amount = serializer.validated_data.get('pay_amount')
        if balance:
            balance += amount
            PayMethod.objects.update_or_create(user=user, defaults={'balance': balance})
            data = {'type': 'Pay successful ! ', 'pay amount': amount, 'balance': balance,
                    'time': datetime.datetime.now()}
            return Response(data)
        else:
            balance += amount
        return Response({'detail': 'Pay successful !'})
