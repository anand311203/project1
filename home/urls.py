from django.urls import path
from django.urls import include


from . import views
urlpatterns = [
   
    path('', views.index , name='home'),
    path('about/', views.about,name='about'),
    path('booking/', views.booking , name='booking'),
    path('doctors', views.doctors , name='doctors'),
    path('contact', views.contact , name='contacts'),
    path('department',views.department , name='department'),
    

]
