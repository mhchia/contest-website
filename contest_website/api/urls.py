from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('get-registrants/', views.get_registrants, name='get-registrants'),
]
