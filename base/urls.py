from django.urls import path

from .views import restaurant_list, restaurant_detail, restaurant_create, restaurant_update, restaurant_delete

app_name = 'base'

urlpatterns = [
    path('restaurant-list/', restaurant_list, name='restaurant-list'),
    path('restaurant-detail/<int:pk>/', restaurant_detail, name='restaurant-detail'),
    path('restaurant-create/<int:pk>/', restaurant_create, name='restaurant-create'),
    path('restaurant-update/<int:pk>/', restaurant_update, name='restaurant-update'),
    path('restaurant-delete/<int:pk>/', restaurant_delete, name='restaurant_delete'),
]
