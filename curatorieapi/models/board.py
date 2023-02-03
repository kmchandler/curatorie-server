from django.db import models

class Board(models.Model):

    type = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.name
