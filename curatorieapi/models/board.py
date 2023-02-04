from django.db import models
from .user import User

class Board(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.name
