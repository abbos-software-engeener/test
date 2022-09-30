from django.db import models


class HomeType(models.Model):
    name = models.CharField(max_length=100)


class Type(models.Model):
    name = models.CharField(max_length=100)


class Home(models.Model):
    home_type = models.ForeignKey(HomeType, on_delete=models.SET_NULL, null=True)
    types = models.ManyToManyField(Type)
    first_payment = models.BooleanField(default=False)
    amount = models.PositiveIntegerField(null=True, blank=True)


class Request(models.Model):
    home = models.ForeignKey(Home, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    is_seen = models.BooleanField(default=False, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-id', '-is_seen')
