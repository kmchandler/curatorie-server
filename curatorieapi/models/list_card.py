from django.db import models

class ListCard(models.Model):

    board_id = models.IntegerField(max_length=100)
    user_id = models.IntegerField(max_length=100)
    list_item = models.TextField(max_length=1000)
    priority = models.BooleanField(default=False)

    def __str__(self):
        return self.list_item
