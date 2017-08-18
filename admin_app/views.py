from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User

from userManagement_app.forms import RegistrationForm, UserChangeForm

from main_app.models import MainService, Service
from .forms import MainServiceForm, ServiceForm

from django.http import Http404, JsonResponse
from django.template import loader
from django.template.context_processors import csrf
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_superuser)
def main_view(request):
    users = User.objects.all()
    user_form = RegistrationForm()
    services = MainService.objects.all()
    return render(request,
                  'myadmin/index.html',
                  {'users': users,
                   'form': user_form,
                   'nbar': 'admin_home',
                   'services': services
                   })

@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/my_admin/')

@user_passes_test(lambda u: u.is_superuser)
def get_user_form(request, user_id):
    if request.is_ajax():
        user = get_object_or_404(User, id=user_id)
        user_form = RegistrationForm(instance=user)
        context = {'form': user_form, 'id': user_id}
        context.update(csrf(request))
        html = loader.render_to_string('registration_form.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404

@user_passes_test(lambda u: u.is_superuser)
def delete_user_form(request, user_id):
    if request.is_ajax():
        user = get_object_or_404(User, id=user_id)
        user.delete()
        users = User.objects.all()
        html = loader.render_to_string('myadmin/users_list.html', {'users': users}, request=request)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404

@user_passes_test(lambda u: u.is_superuser)
def create_user(request, user_id=None):
    """
    Создает Пользователя(User)
    Или редактирует существующего, если указан  user_id
    """
    if request.is_ajax():
        print('user_id = ', user_id)
        if not user_id:
            print('Not user_id')
            user = UserChangeForm(request.POST)
        else:
            user = get_object_or_404(User, id=user_id)
            user = UserChangeForm(request.POST or None, instance=user)
        if user.is_valid():
            user.save()
            users = User.objects.all()
            html = loader.render_to_string('myadmin/users_list.html', {'users': users}, request=request)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        else:
            errors = user.errors.as_json()
            return JsonResponse({'errors': errors})

    raise Http404

# CRUD for models


# Вьюшки для услуг
# Вывод списка услуг
@user_passes_test(lambda u: u.is_superuser)
def admin_list_services(request):
    services = MainService.objects.all()
    services_form = MainServiceForm()
    return render(request,
                  'myadmin/services_view.html',
                  {'services': services,
                   'form': services_form,
                   'nbar': 'admin_services',
                   })


# Заполнение формы услуг данными
@user_passes_test(lambda u: u.is_superuser)
def get_service_form(request, service_id):
    if request.is_ajax():
        service = get_object_or_404(MainService, id=service_id)
        service_form = MainServiceForm(instance=service)
        context = {'form': service_form, 'id': service_id}
        context.update(csrf(request))
        html = loader.render_to_string('registration_form.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404

@user_passes_test(lambda u: u.is_superuser)
def delete_service_form(request, service_id):
    if request.is_ajax():
        service = get_object_or_404(MainService, id=service_id)
        service.delete()
        services = MainService.objects.all()
        html = loader.render_to_string('myadmin/services_list.html', {'services': services}, request=request)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404

@user_passes_test(lambda u: u.is_superuser)
def create_service(request, service_id=None):
    if request.is_ajax():
        print('service_id = ', service_id)
        if not service_id:
            print('Not service_id')
            service = MainServiceForm(request.POST)
        else:
            service = get_object_or_404(MainService, id=service_id)
            service = MainServiceForm(request.POST or None, instance=service)
        if service.is_valid():
            service.save()
            services = MainService.objects.all()
            html = loader.render_to_string('myadmin/services_list.html',
                                           {'services': services},
                                           request=request)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        else:
            errors = service.errors.as_json()
            return JsonResponse({'errors': errors})
    raise Http404


# ---------------------------
@user_passes_test(lambda u: u.is_superuser)
def admin_service_detail(request, pk):
    services = MainService.objects.all()
    service = get_object_or_404(MainService, pk=pk)
    services_list = Service.objects.filter(category=pk)
    services_form = ServiceForm(initial={'category': pk})
    # services_form.fields['category'].widget.attrs['disabled'] = True
    return render(request,
                  'myadmin/service_detail.html',
                  {'nbar': pk,
                   'service': service,
                   'services_list': services_list,
                   'services': services,
                   'form': services_form,
                   })

@user_passes_test(lambda u: u.is_superuser)
def get_service_detail_form(request, service_id):
    if request.is_ajax():
        service = get_object_or_404(Service, id=service_id)
        service_detail_form = ServiceForm(instance=service)
        context = {'form': service_detail_form, 'id': service_id}
        context.update(csrf(request))
        html = loader.render_to_string('registration_form.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404


@user_passes_test(lambda u: u.is_superuser)
def delete_service_detail_form(request, category_id, service_id):
    if request.is_ajax():
        service = get_object_or_404(Service, id=service_id)
        service.delete()
        services_list = Service.objects.filter(category=category_id)
        html = loader.render_to_string('myadmin/service_detail_list.html', {'services_list': services_list}, request=request)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404


@user_passes_test(lambda u: u.is_superuser)
def create_service_detail(request, category_id, service_id=None):
    if request.is_ajax():
        print('service_id = ', service_id)
        if not service_id:
            print('Not service_id')
            service = ServiceForm(request.POST)
        else:
            service = get_object_or_404(Service, id=service_id)
            service = ServiceForm(request.POST or None, instance=service)
        if service.is_valid():
            service.save()
            services_list = Service.objects.filter(category=category_id)
            html = loader.render_to_string('myadmin/service_detail_list.html',
                                           {'services_list': services_list},
                                           request=request)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        else:
            errors = service.errors.as_json()
            return JsonResponse({'errors': errors})
    raise Http404
