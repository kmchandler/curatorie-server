from django.db import models
from .user import User
from .board import Board

class GiftCard(models.Model):

    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    occasion = models.CharField(max_length=50)
    gift_for = models.CharField(max_length=50)
    name = models.CharField(max_length=50, null=True, blank=True)
    priority = models.BooleanField(default=False)

    def __str__(self):
        return self.item
