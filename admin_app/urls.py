from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_view),
    url(r'user/delete/(\d+)$', views.delete_user),
    url(r'user/delete_form/(\d+)$', views.delete_user_form),
    url(r'user/get_user_form/(\d+)$', views.get_user_form),
    url(r'user/create/(\d*)$', views.create_user),
]

urlpatterns += [
    url(r'services/$', views.admin_list_services),
    url(r'services/get_service_form/(\d+)$', views.get_service_form),
    url(r'services/delete_form/(\d+)$', views.delete_service_form),
    url(r'services/create/(\d*)$', views.create_service),
]

urlpatterns += [
    url(r'(?P<pk>[0-9]+)/$', views.admin_service_detail, name='admin_service_detail'),

]
