from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.http import Http404
from .forms import RegistrationForm


def login(request):
    if request.method == 'POST':
        print("POST data =", request.POST)
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            return render(request, 'index.html', {'username': username, 'errors': True})
    raise Http404


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(request, 'registration.html', context)
    context = {'form': RegistrationForm()}
    return render(request, 'registration.html', context)



