from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(decimal_places=5, max_digits=20)
    age = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=50)
    cost = models.DecimalField(decimal_places=5, max_digits=20)
    size = models.DecimalField(decimal_places=5, max_digits=20)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.title

