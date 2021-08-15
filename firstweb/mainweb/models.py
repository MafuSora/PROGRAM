from django.db import models
from django.db.models.deletion import CASCADE, PROTECT

# Create your models here.
# categori = laptop --> DEL laptop
# laptop = chromebook --> laptop -->


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=PROTECT)


# class Buyer(models.Model):
#     name = models.TextField()
#     alamat = models.TextField()
#     nope = models.TextField()


class Review(models.Model):
    # name = models.ForeignKey(Buyer, on_delete=CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    review = models.TextField()
    product = models.ForeignKey(Product, on_delete=CASCADE)


# py manage.py makemigrations
# py manage.py migrate
# py manage.py createsuperuser
# root root12345
# py manage.py runseerver
