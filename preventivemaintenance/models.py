from django.db import models
from home.models import Device


class PM(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='pmdevice', blank=False, null=False)

    def __str__(self):
        return f"{self.device.name}'s preventive maintenance"


class DailySchedule(models.Model):
    daily_schedule = models.CharField(max_length=500, null=False, blank=False , default='pm')
    pm = models.ForeignKey(PM, on_delete=models.CASCADE, related_name='dailypm')

    def __str__(self):
        return f"{self.pm.device.name}'s preventive maintenance"


class WeeklySchedule(models.Model):
    weekly_schedule = models.CharField(max_length=500, null=False, blank=False , default='pm')
    pm = models.ForeignKey(PM, on_delete=models.CASCADE, related_name='weekpm')

    def __str__(self):
        return f"{self.pm.device.name}'s preventive maintenance"


class MonthlySchedule(models.Model):
    monthly_schedule = models.CharField(max_length=500,  null=False, blank=False , default='pm')
    pm = models.ForeignKey(PM, on_delete=models.CASCADE, related_name='monthpm')

    def __str__(self):
        return f"{self.pm.device.name}'s preventive maintenance"


class SeasonSchedule(models.Model):
    season_schedule = models.CharField(max_length=500,  null=False, blank=False , default='pm')
    pm = models.ForeignKey(PM, on_delete=models.CASCADE, related_name='seasonpm')

    def __str__(self):
        return f"{self.pm.device.name}'s preventive maintenance"


class SixMonthSchedule(models.Model):
    sixmonth_schedule = models.CharField(max_length=500,  null=False, blank=False , default='pm')
    pm = models.ForeignKey(PM, on_delete=models.CASCADE, related_name='sixmonthpm')

    def __str__(self):
        return f"{self.pm.device.name}'s preventive maintenance"


class YearSchedule(models.Model):
    yearly_schedule = models.CharField(max_length=500,  null=False, blank=False , default='pm')
    pm = models.ForeignKey(PM, on_delete=models.CASCADE, related_name='yearpm')

    def __str__(self):
        return f"{self.pm.device.name}'s preventive maintenance"
