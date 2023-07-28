from business.models import business, BusinessType
from django.shortcuts import render
from health_service.models import HealthService, HealthType
from temple.models import Temple

from .models import LookupField


# Create your views here.

def homepage(request, id=1):
    business_type = BusinessType.objects.all()
    health_type = HealthType.objects.all()
    business_data = business.objects.filter(business_type_id=id)
    try:
        banner = LookupField.objects.get(code='main banner')
        banner_img = banner.image.url
    except:
        banner_img = ''
    context = {
        'business_type': business_type,
        'health_type': health_type,
        'banner_img': banner_img,
        'business': business_data
    }

    return render(request, 'index.html', context)


def visiting(request, id):
    view_business = business.objects.get(id=id)
    context = {
        'business_details': view_business
    }
    return render(request, 'visiting.html', context)


def hospital(request, id):
    business_type = BusinessType.objects.all()
    health_type = HealthType.objects.all()
    hospital_data = HealthService.objects.filter(type_id=id)
    try:
        banner = LookupField.objects.get(code='main banner')
        banner_img = banner.image.url
    except:
        banner_img = ''
    context = {
        'banner_img': banner_img,
        'business_type':business_type,
        'health_type': health_type,
        'hospital': hospital_data
    }

    return render(request, 'hospital.html', context)


def temple(request):
    business_type = BusinessType.objects.all()
    health_type = HealthType.objects.all()
    temple = Temple.objects.all()
    try:
        banner = LookupField.objects.get(code='main banner')
        banner_img = banner.image.url
    except:
        banner_img = ''
    context = {
        'banner_img': banner_img,
        'business_type': business_type,
        'health_type': health_type,
        'temple': temple
    }

    return render(request, 'temple_list.html', context)
