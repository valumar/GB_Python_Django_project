from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.service_list_view),
    url(r'^(?P<pk>[0-9]+)/$', views.service_detail, name='service_detail'),
]


