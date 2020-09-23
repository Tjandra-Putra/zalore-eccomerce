from django.db import models
from django.utils import timezone
import datetime

# After making changes to the field, make sure to cmd : python manage.py makemigrations & python manage.py migrate
# Basically to make changes

class Support(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    message = models.TextField()
    date_sent = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):  # For easier visualisation when being printed in the cmd
        return self.first_name  # Output display : <QuerySet [<Support: Tjandra>]>


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.TextField(null=True)
    product_image = models.ImageField(default='default.PNG', upload_to='img_product')
    product_price = models.FloatField(default=0)
    product_discount = models.FloatField(default=0)
    product_stock = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name