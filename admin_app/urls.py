from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_view),
    url(r'user/delete/(\d+)$', views.delete_user),
    url(r'user/delete_form/(\d+)$', views.delete_user_form),
    url(r'user/get_user_form/(\d+)$', views.get_user_form),
    url(r'user/create/(\d*)$', views.create_user),
]
