from business.models import business, BusinessType
from django.shortcuts import render
from health_service.models import HealthService, HealthType
from store.models import StoreType, Store
from temple.models import Temple

from .models import LookupField

from education_sector.models import Type as EducationType
from education_sector.models import EducationSector

# Create your views here.

def homepage(request, id=1):
    store_type = StoreType.objects.all()
    business_type = BusinessType.objects.all()
    health_type = HealthType.objects.all()
    education_type = EducationType.objects.all()
    business_data = business.objects.filter(business_type_id=id)
    try:
        banner = LookupField.objects.get(code='main banner')
        banner_img = banner.image.url
    except:
        banner_img = ''

    context = {
        'store_type': store_type,
        'business_type': business_type,
        'health_type': health_type,
        'banner_img': banner_img,
        'business': business_data,
        'education_type': education_type,
    }

    return render(request, 'index.html', context)


def education(request, id):
    store_type = StoreType.objects.all()
    business_type = BusinessType.objects.all()
    health_type = HealthType.objects.all()
    education_type = EducationType.objects.all()
    education = EducationSector.objects.filter(type_id=id)

    try:
        banner = LookupField.objects.get(code='main banner')
        banner_img = banner.image.url
    except:
        banner_img = ''

    context = {
        'store_type': store_type,
        'banner_img': banner_img,
        'business_type': business_type,
        'health_type': health_type,
        'education': education,
        'education_type': education_type,
    }

    return render(request, 'education.html', context)


def visiting(request, id):
    store_type = StoreType.objects.all()
    business_type = BusinessType.objects.all()
    health_type = HealthType.objects.all()

    view_business = business.objects.get(id=id)
    context = {
        'store_type' : store_type,
        'business_type' : business_type,
        'health_type' : health_type,
        'business_details': view_business
    }
    return render(request, 'visiting.html', context)


def hospital(request, id):
    store_type = StoreType.objects.all()
    business_type = BusinessType.objects.all()
    health_type = HealthType.objects.all()
    hospital_data = HealthService.objects.filter(type_id=id)
    try:
        banner = LookupField.objects.get(code='main banner')
        banner_img = banner.image.url
    except:
        banner_img = ''
    context = {
        'store_type' : store_type,
        'banner_img': banner_img,
        'business_type': business_type,
        'health_type': health_type,
        'hospital': hospital_data
    }

    return render(request, 'hospital.html', context)


def temple(request):
    store_type = StoreType.objects.all()
    business_type = BusinessType.objects.all()
    health_type = HealthType.objects.all()
    temple = Temple.objects.all()
    try:
        banner = LookupField.objects.get(code='main banner')
        banner_img = banner.image.url
    except:
        banner_img = ''
    context = {
        'store_type' : store_type,
        'banner_img': banner_img,
        'business_type': business_type,
        'health_type': health_type,
        'temple': temple
    }

    return render(request, 'temple_list.html', context)


def business_unite(request, id):
    store_type = StoreType.objects.all()
    business_type = BusinessType.objects.all()
    health_type = HealthType.objects.all()
    business_unite = Store.objects.filter(store_type_id=id)
    try:
        banner = LookupField.objects.get(code='main banner')
        banner_img = banner.image.url
    except:
        banner_img = ''
    context = {
        'store_type': store_type,
        'banner_img': banner_img,
        'business_type': business_type,
        'health_type': health_type,
        'business_unite': business_unite,
    }

    return render(request, 'business_unit.html', context)


