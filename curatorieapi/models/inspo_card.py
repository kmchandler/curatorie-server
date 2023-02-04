from django.db import models
from .user import User
from .board import Board

class InspoCard(models.Model):

    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    priority = models.BooleanField(default=False)

    def __str__(self):
        return self.description
