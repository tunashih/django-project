from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mysite-home'),
    path('about/', views.about, name='mysite-about'),
    path('search/', views.search, name='mysite-search'),
    path('search_results/', views.search_results, name='mysite-search_results'),
]