from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50)
    colors = models.JSONField(blank=True, null=True)  # Can store multiple colors 
    photo = models.ImageField(upload_to='products/photos/', blank=True, null=True)

    def __str__(self):
        return self.name

