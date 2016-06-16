from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse, reverse_lazy

from ecom.utils.mixins import AjaxableResponseMixin, CreateView, UpdateView, DeleteView
from inventory.forms import UnitForm
from inventory.models import Item, Unit


def home(request):
    return render(request, 'inventory/home.html')


class UnitDetailView(DetailView):
    model = Unit


class UnitView(object):
    model = Unit
    success_url = reverse_lazy('unit_list')
    form_class = UnitForm


class UnitListView(UnitView, ListView):
    pass


class UnitCreate(AjaxableResponseMixin, UnitView, CreateView):
    pass


class UnitUpdate(UnitView, UpdateView):
    pass


class UnitDelete(UnitView, DeleteView):
    pass

class ItemDetailView(DetailView):
    model = Item
