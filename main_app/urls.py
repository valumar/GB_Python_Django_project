from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.service_list_view),
    url(r'^$', views.ServiceListView.as_view()),
    # url(r'^(?P<pk>[0-9]+)/$', views.service_detail, name='service_detail'),
    url(r'^(?P<service_id>[0-9]+)/$', views.ServiceDetailView.as_view(), name='service_detail'),
]


