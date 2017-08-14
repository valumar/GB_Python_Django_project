from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    service_detail_list = Service.objects.filter(category=pk)
    paginator = Paginator(service_detail_list, 5)
    page = request.GET.get('page')
    try:
        service_list = paginator.page(page)
    except PageNotAnInteger:
        service_list = paginator.page(1)
    except EmptyPage:
        paginator.page(paginator.num_pages)
    return render(request,
                  'service_detail.html',
                  {'nbar': '',
                   'service': service,
                   'service_list': service_list,
                   'services': services
                   })
