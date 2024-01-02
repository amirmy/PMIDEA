from django.contrib import admin
from .models import FirstLevelCategory, Device, SecondLevelCategory


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created', 'risk_class', 'display_status')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('author', 'risk_class',)
    ordering = ('created',)
    search_fields = ('name', 'author__name', 'risk_class',)
    fieldsets = (
        ('main', {'fields': ('name', 'author', 'description', 'history', 'slug',
                             'display_status')}),
        ('channel', {'fields': ('first_level_category', 'second_level_category')}),
        ('ids', {'fields': ('risk_class', 'UMDNS', 'modality')})
    )
    filter_horizontal = ()
    actions = ['make_withdraw', 'make_draft', 'make_publish']

    @admin.action(description='make publish selected devices')
    def make_publish(self, request, query_set):
        query_set.update('p')

    @admin.action(description='make draft selected devices')
    def make_draft(self, request, query_set):
        query_set.update('d')

    @admin.action(description='make withdraw selected devices')
    def make_withdraw(self, request, query_set):
        query_set.update('w')


admin.site.register(Device, DeviceAdmin)
admin.site.register(FirstLevelCategory)
admin.site.register(SecondLevelCategory)
