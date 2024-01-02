from django.db import models
from home.models import Device


class BuyDevice(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='buy_device', null=False, blank=False)
    Description = models.CharField(max_length=800)
    amount_consumption_per_patient = models.IntegerField(default=0)
    price_per_consumption = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.device.name} buy condition'


class BuyBrand(models.Model):
    buy_device = models.ForeignKey(BuyDevice, on_delete=models.CASCADE, related_name='by_brand', null=False,
                                   blank=False)
    ppc_brand = models.DecimalField(max_digits=10, decimal_places=2)
    warranty = models.IntegerField()
    special_warranty = models.IntegerField()
    special_warranty_description = models.CharField()

    def __str__(self):
        return f"{self.buy_device.device.name}'s brand condition"
