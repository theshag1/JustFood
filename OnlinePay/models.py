from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


# Create your models here.


def validate_card_number(value):
    if not value.startswith(('8600', '9860',)):
        raise ValidationError(_('Card number must start 8600 , 9860\nPlease input correct Card number'))


class PayMethod(models.Model):
    card_choices = [
        ('Uzcard', 'uzcard'),
        ('Humo', 'humo'),
        ('Visa', 'visa'),
        ('Unionpay', 'unionpay'),
        ('Mastercard', 'mastercard')
    ]
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='pay_user')
    card_type = models.CharField(
        choices=card_choices,
        max_length=50,
        help_text=_(
            "Select card for your payment "
        ),
        error_messages={
            'detail': _('You dont select card for payment !')
        }

    )
    card_number = models.CharField(
        unique=True,
        validators=[validate_card_number],
        error_messages={'detail': _('Please enter the correct card number')}

    )

    created_at = models.DateTimeField(auto_now=True)
    pay_amount = models.BigIntegerField()
    balance = models.BigIntegerField(null=True)

    def __str__(self):
        return f'{self.user}  :   {self.pay_amount}'
