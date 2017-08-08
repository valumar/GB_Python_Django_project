from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from userManagement_app.forms import RegistrationForm
from django.contrib.auth.decorators import user_passes_test


# доступ у админке только суперпользователю
# @user_passes_test(lambda u: u.is_superuser)
def main_view(request):
    users = User.objects.all()
    user_form = RegistrationForm()
    return render(request, 'admin/index.html', {'users': users, 'form': user_form})


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/my_admin/')


def create_user(request, user_id):
    pass
