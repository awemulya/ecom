from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from inventory.models import Item, Unit


def home(request):
    return render(request,'inventory/home.html')


class UnitDetailView(DetailView):
    model = Unit


class UnitListView(ListView):
    model = Unit


class ItemDetailView(DetailView):

    model = Item
