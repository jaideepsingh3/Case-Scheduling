from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('createnewaccount/', views.create_account_view, name='createnewaccount'),
]