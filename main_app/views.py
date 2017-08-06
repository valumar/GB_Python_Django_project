from django.shortcuts import render
from .models import MainService

def main_view(request):
    services = MainService.objects.all()
    return render(request, 'index.html', {'nbar': 'home', 'services': services})
