from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import RestaurantForm


class RestaurantsView(TemplateView):
    template_name = 'index.html'


class CreateRestaurantView(FormView):
    template_name = 'create.html'
    form_class = RestaurantForm
    success_url = reverse_lazy('app:restaurants-view')


def update_restaurant(request):
    return render(request, 'update.html')
