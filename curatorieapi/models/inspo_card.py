from django.db import models

class InspoCard(models.Model):

    image_url = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    priority = models.BooleanField(default=False)

    def __str__(self):
        return self.description
