from django.shortcuts import render
from .models import Test, Mayo_doct


def test(request):
    obj = Test.objects.all()
    return render(request, 'testdata.html', {'obj': obj})


def home(request):
    return render(request, 'home.html')


def nav(request):
    return render(request, 'nav.html')

def footer(request):
    return render(request, 'footer.html')


def doctors(request):
    obj_doctors = Mayo_doct.objects.all()
    return render(request, 'mayo_doctors.html', {'obj_doctors': obj_doctors})


def mayo_patient_registration(request):
    return render(request, 'mayo_patient_registration.html')

def abc(request, name):
    patiend_detail =
    return render(request,)


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')

def vinod(request, period):
    data = {1:{"user": "cnu", "spoolTime": "12.13.4", "status": "dfg", "priority":108},
            2:{"user": "vino", "spoolTime": "12.13.4", "status": "Done", "priority":208},
            3:{"user": "abd", "spoolTime": "12.13.4", "status": "Do", "priority":10}}
    return render(request, 'tabletask.html', {'data':data})