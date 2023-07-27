from django.shortcuts import render
from business.models import business
from health_service.models import HealthService
from .models import LookupField
# Create your views here.

def homepage(request):
    business_data = business.objects.all()
    banner = LookupField.objects.get(code='main banner')
    banner_img = banner.image.url
    context = {
        'banner_img':banner_img,
        'business':business_data
    }

    return render(request,'index.html',context)

def visiting(request,id):
    view_business = business.objects.get(id=id)
    context = {
        'business_details':view_business
    }
    return render(request,'visiting.html',context)

def hospital(request):
    hospital_data = HealthService.objects.filter(type_id=2)
    banner = LookupField.objects.get(code='main banner')
    banner_img = banner.image.url
    context = {
        'banner_img':banner_img,
        'hospital':hospital_data
    }

    return render(request,'hospital.html',context)
