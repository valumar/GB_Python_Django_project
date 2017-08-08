from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_view),
    url(r'^delete/user/(\d+)$', views.delete_user),
    url(r'^create/user/(\d+)$', views.create_user),
]