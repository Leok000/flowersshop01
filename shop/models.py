from django.db import models


class ShopModels(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='uploads', null=True)
    in_stock = models.BooleanField(default=True)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.name
