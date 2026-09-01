from django.contrib import admin
from django.contrib.auth.admin import Group
from django.contrib.auth.admin import GroupAdmin
from .models import ServiceRecord, WheelService, PartSale


admin.site.unregister(Group)


@admin.register(Group)
class CustomGroupAdmin(GroupAdmin):
    filter_horizontal = ('permissions',)


admin.site.register(ServiceRecord)
admin.site.register(WheelService)
admin.site.register(PartSale)
