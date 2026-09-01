from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path(
        'add-service/',
        views.ServiceRecordCreateView.as_view(),
        name='service-create',
    ),
    path(
        'add-wheel/',
        views.WheelServiceCreateView.as_view(),
        name='wheel-create',
    ),
    path(
        'add-part/',
        views.PartSaleCreateView.as_view(),
        name='part-create',
    ),
    path(
        '<int:pk>/edit/',
        views.ServiceUpdateView.as_view(),
        name='service-update',
    ),
    path(
        '<int:pk>/delete/',
        views.ServiceDeleteView.as_view(),
        name='service-delete',
    ),
    path(
        'service/<int:pk>/',
        views.service_detail,
        name='service_detail'
    ),
]
