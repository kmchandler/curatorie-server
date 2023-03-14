from django.db import models

class User(models.Model):

    uid = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    image_url = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + self.last_name
