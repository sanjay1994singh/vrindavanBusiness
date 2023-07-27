from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage,name='homepage'),
    path('visiting/<int:id>/', views.visiting,name='visiting'),
    path('hospital/', views.hospital,name='hospital'),
]
