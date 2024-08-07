from django.contrib import admin
from .models import CarList,ShowroomList
# Register your models here.
class showlist(admin.ModelAdmin):
    list_display=['name','desc','active']

class showroom(admin.ModelAdmin):
    list_display=['name','desc','website','location']

admin.site.register(CarList,showlist)
admin.site.register(ShowroomList,showroom)