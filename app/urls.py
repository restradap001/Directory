from django.urls import path
from .views import RestaurantsView, CreateRestaurantView, update_restaurant

app_name = 'app'

urlpatterns = [
    path('', RestaurantsView.as_view(), name='restaurants-view'),
    path('restaurants/create/', CreateRestaurantView.as_view(), name='create-restaurant-view'),
    path('restaurants/update/', update_restaurant, name='update-restaurants-view'),
]