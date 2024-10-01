from django.urls import path 
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    # path('pay/', views.pay, name='pay'),
    # path('success/', views.success, name='success'),
    # path('cancel/', views.cancel, name='cancel'),
]