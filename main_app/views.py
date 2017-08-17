from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import MainService, Service
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView, TemplateView
from django.views.generic.base import ContextMixin


# def main_view(request):
#     services = MainService.objects.all()
#     return render(request, 'index.html', {'nbar': 'home', 'services': services})


# Миксин для меню в _base.html
class MainServiceMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services = MainService.objects.all()
        context['services'] = services
        return context


# Главная страница
class MainView(TemplateView, MainServiceMixin):
    template_name = 'index.html'


# def service_list_view(request):
#     services = MainService.objects.all()
#     return render(request, 'services_list.html', {'nbar': 'home', 'services': services})


# Запасная страница со списком услуг
class ServiceListView(TemplateView, MainServiceMixin):
    template_name = 'services_list.html'


class ServiceDetailView(ListView, MainServiceMixin):

    def get(self, request, *args, **kwargs):
        self.service_id = kwargs['service_id']
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = MainService.objects.get(pk=self.service_id)
        context['service'] = service
        return context

    def get_queryset(self):
        service_detail_list = Service.objects.filter(category__id=self.service_id)
        return service_detail_list

    model = Service
    template_name = 'service_detail.html'
    paginate_by = 2
    context_object_name = 'service_list'

#
# def service_detail(request, pk):
#     services = MainService.objects.all()
#     service = get_object_or_404(MainService, pk=pk)
#     service_detail_list = Service.objects.filter(category=pk)
#     paginator = Paginator(service_detail_list, 5)
#     page = request.GET.get('page')
#     try:
#         service_list = paginator.page(page)
#     except PageNotAnInteger:
#         service_list = paginator.page(1)
#     except EmptyPage:
#         paginator.page(paginator.num_pages)
#     return render(request,
#                   'service_detail.html',
#                   {'nbar': '',
#                    'service': service,
#                    'service_list': service_list,
#                    'services': services
#                    })
