from django.db import models

class BoardType(models.Model):
    type = models.CharField(max_length=50)

def __str__(self):
    return self.type
