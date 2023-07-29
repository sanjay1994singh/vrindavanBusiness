from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('temple/', views.temple, name='homepage'),
    path('<int:id>/', views.homepage, name='homepage'),
    path('visiting/<int:id>/', views.visiting, name='visiting'),
    path('hospital/<int:id>/', views.hospital, name='hospital'),
    path('business-unite/<int:id>/', views.business_unite, name='business_unite'),
]
