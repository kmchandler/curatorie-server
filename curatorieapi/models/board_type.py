from django.db import models
from .board import Board

class BoardType(models.Model):

    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

def __str__(self):
    return self.type
