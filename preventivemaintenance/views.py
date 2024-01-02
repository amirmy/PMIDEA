from django.shortcuts import render, get_object_or_404
from .models import *


def preventivemaintenance_view(request, slug):
    device = Device.objects.get(slug=slug)
    daily_pm = DailySchedule.objects.filter(pm__device=device)
    weekly_schedule = WeeklySchedule.objects.filter(pm__device=device)
    monthly_schedule = MonthlySchedule.objects.filter(pm__device=device)
    season_schedule = SeasonSchedule.objects.filter(pm__device=device)
    sixmonth_schedule = SixMonthSchedule.objects.filter(pm__device=device)
    yearly_schedule = YearSchedule.objects.filter(pm__device=device)
    content = {'daily_pm': daily_pm,
               'weekly_schedule': weekly_schedule,
               'monthly_schedule': monthly_schedule,
               'season_schedule': season_schedule,
               'sixmonth_schedule': sixmonth_schedule,
               'yearly_schedule': yearly_schedule}
    return render(request, 'PM/pm_view.html', content)
