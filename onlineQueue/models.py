from django.db import models


# Create your models here.

class Queue(models.Model):
    queue = models.SmallIntegerField(unique=False, null=False)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='user_queue')
    is_being_prepared = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f'{self.queue} : {self.user}'
