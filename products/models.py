from django.shortcuts import reverse
from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products_images')
    category = models.CharField(max_length=60)

    def get_detail_url(self):
        return reverse('products:detail', args=[self.pk])
