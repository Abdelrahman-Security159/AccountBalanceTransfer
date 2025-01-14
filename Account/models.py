from django.db import models

# Create your models here.
class Account(models.Model):
    account_id = models.CharField(max_length=64, blank=False, null=False)
    username   = models.CharField(max_length=256, blank=False, null=False)
    balance    = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.account_id} - {self.balance}"