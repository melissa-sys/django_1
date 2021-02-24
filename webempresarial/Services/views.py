from django.shortcuts import render
from .models import Service

# Create your views here.


def services(request):
    services = Service.objects.all()  # IMPORTANTÍSIMO
    return render(request, 'services/services.html', {'services': services})
