from django.contrib import admin
from .models import CarList
# Register your models here.
class showlist(admin.ModelAdmin):
    list_display=['name','desc','active']

admin.site.register(CarList,showlist)