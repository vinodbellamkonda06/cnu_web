from django.conf.urls import url,include
from .import views

urlpatterns = [
    url(r'home', views.home),
    url(r'test', views.test),
    url(r'nav', views.nav),
    url(r'doctors', views.doctors),
    url(r'registration', views.mayo_patient_registration),
    url(r'services', views.services),
    url(r'contact', views.contact),
    url(r'footer', views.footer),
    url(r'vinod', views.vinod),
]