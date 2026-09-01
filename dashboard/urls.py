from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
     path('', views.dashboard, name='dashboard_index'),
     path(
          'service/create/',
          views.ServiceCreateView.as_view(),
          name='service-create',
     ),
     path(
          'wheel/create/',
          views.WheelCreateView.as_view(),
          name='wheel-create',
     ),
]
