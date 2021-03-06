from django.db import models

# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=30)
    email_id = models.EmailField()
    contact = models.IntegerField()
    balance = models.IntegerField()

    def __str__(self):
        return self.username


class Deposit(models.Model):
    username = models.CharField(max_length=30)
    email_id = models.EmailField()
    contact = models.IntegerField()
    amount = models.IntegerField("Amount (₹)")

    def str(self):
        return self.username


class Transact(models.Model):
    username = models.CharField(max_length=30)
    email_id = models.EmailField()
    contact = models.IntegerField()
    amount = models.IntegerField("Amount (₹)")
    receiver = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class History(models.Model):
    username = models.CharField(max_length=30)
    email_id = models.EmailField()
    contact = models.IntegerField()
    amount = models.IntegerField("Amount (₹)")
    action = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.username