from django.db import models

class ListCard(models.Model):

    list_item = models.TextField(max_length=1000)
    priority = models.BooleanField(default=False)

    def __str__(self):
        return self.list_item
