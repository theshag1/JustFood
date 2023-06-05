from django.db import models


# Create your models here.
class PayAction(models.Model):
    pay_method = models.ForeignKey('OnlinePay.PayMethod', on_delete=models.CASCADE, related_name='pay_action')
    user = models.CharField()
    balance = models.CharField()


