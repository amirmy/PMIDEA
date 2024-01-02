from django.shortcuts import render, get_object_or_404
from .models import BuyDevice, Device, BuyBrand
#from .forms import BuyDeviceFormSet, BuyBrandFormSet



def buy_device(request, slug):
    device = get_object_or_404(Device, slug=slug)
    buydevice = get_object_or_404(BuyDevice, device=device)
    buybrand = get_object_or_404(BuyBrand, buy_device=buydevice)
    return render(request, 'buy/buy_view.html', {'device': device, 'buydevice': buydevice, 'buybrand': buybrand})


def create_buy(request):
    if request.method == 'POST':
        buy_device_formset = BuyDeviceFormSet(request.POST, prefix='buy_device')
        buy_brand_formset = BuyBrandFormSet(request.POST, prefix='buy_brand')
        if buy_device_formset.is_valid() and buy_brand_formset.is_valid():
            # ذخیره اطلاعات خرید دستگاه
            buy_device_instances = buy_device_formset.save(commit=False)
            for buy_device_instance in buy_device_instances:
                # اطلاعات خرید دستگاه را ذخیره کنید
                buy_device_instance.save()

            # ذخیره اطلاعات برند
            buy_brand_instances = buy_brand_formset.save(commit=False)
            for i, buy_brand_instance in enumerate(buy_brand_instances):
                # متناسب با هر buy_device_instance اطلاعات برند را ذخیره کنید
                buy_brand_instance.buy_device = buy_device_instances[i]
                buy_brand_instance.save()

    else:
        buy_device_formset = BuyDeviceFormSet(prefix='buy_device')
        buy_brand_formset = BuyBrandFormSet(prefix='buy_brand')

    return render(request, 'buy/create_buy.html',
                  {'buy_device_formset': buy_device_formset, 'buy_brand_formset': buy_brand_formset})