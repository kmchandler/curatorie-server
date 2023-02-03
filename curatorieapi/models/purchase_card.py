from django.db import models

class PurchaseCard(models.Model):

    link = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    priority = models.BooleanField(default=False)

    def __str__(self):
        return self.item
