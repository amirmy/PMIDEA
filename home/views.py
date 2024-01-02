from django.shortcuts import render, get_object_or_404
from .models import Device, FirstLevelCategory


def home_index(request, slug=None):
    device = Device.objects.all()
    first_levels = FirstLevelCategory.objects.all()
    return render(request, 'home/index_home.html',
                  {'device': device, 'first_levels': first_levels})


def device_detail(request, slug):
    device = get_object_or_404(Device, slug=slug)
    return render(request, 'home/device_detail.html', {'device': device})
