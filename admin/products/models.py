from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=200)
    stock = models.IntegerField(default=0)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def rating(self):
        review = Product.objects.filter(stars=self)
        return review


class User(models.Model):
    pass