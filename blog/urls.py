from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('service_detail/', views.service_detail, name='service_detail'),
]