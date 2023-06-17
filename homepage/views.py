from django.shortcuts import render
from business.models import business
# Create your views here.

def homepage(request):
    business_data = business.objects.all()
    
    context = {
        'business':business_data
    }
    return render(request,'index.html',context)

def visiting(request,id):
    view_business = business.objects.get(id=id)
    context = {
        'business_details':view_business
    }
    return render(request,'visiting.html',context)
