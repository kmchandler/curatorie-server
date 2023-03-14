from django.db import models
from .user import User
from .board import Board


class ShareRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'board'], name='unique_share')
        ]
