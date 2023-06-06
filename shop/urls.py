from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('catalog/', views.catalog, name='catalog'),
    path('delivery/', views.delivery, name='delivery'),
    path('contacts/', views.contacts, name='contacts'),
    path('catalog/contacts/', views.contacts, name='catalog/contacts')
]
