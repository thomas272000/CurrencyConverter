from django.db import models

# Create your models here.
class ConversionModel(models.Model):
    from_currency = models.CharField(max_length=3)
    to_currency = models.CharField(max_length=3)
    amount = models.FloatField()
    converted_amount = models.FloatField()
    rate = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    