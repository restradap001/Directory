from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RestaurantSerializer
from .models import Restaurant, RestaurantType


@api_view(['GET'])
def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurants, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def restaurant_detail(request, pk):
    restaurant = Restaurant.objects.get(id=pk)
    serializer = RestaurantSerializer(restaurant, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def restaurant_create(request, pk):
    serializer = RestaurantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def restaurant_update(request, pk):
    restaurant = Restaurant.objects.get(id=pk)
    serializer = RestaurantSerializer(instance=restaurant, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def restaurant_delete(request, pk):
    restaurant = Restaurant.objects.get(id=pk)
    restaurant.delete()
    return Response('The Selected Restaurant Was Deleted')
