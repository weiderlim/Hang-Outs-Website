from django.urls import path
from . import views 

urlpatterns = [
    path('', views.view_search, name='maps_app_view_search'),
    path('results/', views.view_results, name='maps_app_view_results'),
    path('info/', views.view_info, name='maps_app_view_info'), 
]


