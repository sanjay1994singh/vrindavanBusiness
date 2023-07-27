from django.contrib import admin
from .models import HealthType,HealthService
# Register your models here.

admin.site.register(HealthType)
admin.site.register(HealthService)
