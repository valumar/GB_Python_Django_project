from django.shortcuts import render, get_object_or_404
from .models import MainService, Service


def main_view(request):
    services = MainService.objects.all()
    return render(request, 'index.html', {'nbar': 'home', 'services': services})


def service_list_view(request):
    services = MainService.objects.all()
    return render(request, 'services_list.html', {'nbar': 'home', 'services': services})


def service_detail(request, pk):
    services = MainService.objects.all()
    service = get_object_or_404(MainService, pk=pk)
    services_list = Service.objects.filter(category=pk)

    return render(request,
                  'service_detail.html',
                  {'nbar': '',
                   'service': service,
                   'services_list': services_list,
                   'services': services
                   })
