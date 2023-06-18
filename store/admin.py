from django.contrib import admin
from .models import Store,StoreType
# Register your models here.

admin.site.register(StoreType)
admin.site.register(Store)
