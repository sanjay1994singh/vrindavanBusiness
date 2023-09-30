from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('temple/', views.temple, name='homepage'),
    path('<int:id>/', views.homepage, name='homepage'),
    path('visiting/<int:id>/', views.visiting, name='visiting'),
    path('adhyatm/<int:id>/', views.adhyatm, name='adhyatm'),
    path('education/<int:id>/', views.education, name='education'),
    path('hospital/<int:id>/', views.hospital, name='hospital'),
    path('business-unite/<int:id>/', views.business_unite, name='business_unite'),
]
