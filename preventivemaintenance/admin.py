from django.contrib import admin
from .models import *


class DailyScheduleInLineAdmin(admin.TabularInline):
    model = DailySchedule
    extra = 1  # تعداد اضافی مورد‌ها که می‌توانید اضافه کنید


class WeeklyScheduleInLineAdmin(admin.TabularInline):
    model = WeeklySchedule
    extra = 1  # تعداد اضافی مورد‌ها که می‌توانید اضافه کنید


class MonthlyScheduleInLineAdmin(admin.TabularInline):
    model = MonthlySchedule
    extra = 1  # تعداد اضافی مورد‌ها که می‌توانید اضافه کنید


class SeasonScheduleInLineAdmin(admin.TabularInline):
    model = SeasonSchedule
    extra = 1  # تعداد اضافی مورد‌ها که می‌توانید اضافه کنید


class SixMonthScheduleInLineAdmin(admin.TabularInline):
    model = SixMonthSchedule
    extra = 1  # تعداد اضافی مورد‌ها که می‌توانید اضافه کنید


class YearScheduleScheduleInLineAdmin(admin.TabularInline):
    model = YearSchedule
    extra = 1 # تعداد اضافی مورد‌ها که می‌توانید اضافه کنید


class PMAdmin(admin.ModelAdmin):
    inlines = (DailyScheduleInLineAdmin, WeeklyScheduleInLineAdmin, MonthlyScheduleInLineAdmin,
               SeasonScheduleInLineAdmin, SeasonScheduleInLineAdmin, YearScheduleScheduleInLineAdmin)


admin.site.register(PM, PMAdmin)
