from django.db import models


class Register(models.Model):
    username = models.CharField(max_length=30, default="shinu")
    email = models.EmailField(max_length=30, default="shinu@gmail.com")
    password = models.CharField(max_length=20, default=12345)

    def __str__(self):
        return self.username

class create_an_account(models.Model):
    Register = models.OneToOneField(
        Register,
        on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=30, blank=True, null=True)
    Mobile = models.PositiveIntegerField(default=1234567898)
    address = models.CharField(max_length=200)
    PIN = models.IntegerField(default=12345678)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    account_type = models.CharField(max_length=20, default="savings")
    initial_balance = models.IntegerField(default=000)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username
