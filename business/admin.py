from django.contrib import admin
from .models import FoodType,FoodList,Facility,FoodCategory,business,BusinessType

# Register your models here.

admin.site.register(FoodType)
admin.site.register(FoodList)
admin.site.register(Facility)
admin.site.register(FoodCategory)
admin.site.register(business)
admin.site.register(BusinessType)