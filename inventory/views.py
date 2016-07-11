from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse, reverse_lazy

from ecom.utils.mixins import AjaxableResponseMixin, CreateView, UpdateView, DeleteView
from inventory.forms import UnitForm, ItemForm, CompanyForm
from inventory.models import Item, Unit, Company
from inventory.serializer.serializer import ItemSerializer


def home(request):
    return render(request, 'inventory/home.html')


class UnitDetailView(DetailView):
    model = Unit


class UnitView(object):
    model = Unit
    success_url = reverse_lazy('unit_list')
    form_class = UnitForm


class CompanyView(object):
    model = Company
    success_url = reverse_lazy('unit_list')
    form_class = CompanyForm


class UnitListView(UnitView, ListView):
    pass


class UnitCreate(AjaxableResponseMixin, UnitView, CreateView):
    pass

class CompanyCreate(AjaxableResponseMixin, CompanyView, CreateView):
    pass


class UnitUpdate(UnitView, UpdateView):
    pass


class UnitDelete(UnitView, DeleteView):
    pass


def item(request, pk=None):
    if pk:
        item_obj = get_object_or_404(Item, id=pk)
        scenario = 'Update'
        unit = item_obj.unit.id
    else:
        item_obj = Item()
        scenario = 'Create'
        unit = ''
    if request.POST:
        form = ItemForm(data=request.POST, instance=item_obj, request=request)
        if form.is_valid():
            item_obj = form.save(commit=False)
            property_name = request.POST.getlist('property_name')
            item_property = request.POST.getlist('property')
            unit_id = request.POST.get('unit')
            item_obj.unit_id = int(unit_id)
            if request.FILES != {}:
                pass
                # item_obj.image = request.FILES['image']
            other_properties = {}
            for key, value in zip(property_name, item_property):
                if key and value:
                    other_properties[key] = value
            if other_properties: item_obj.other_properties = other_properties
            item_obj.save(account_no=form.cleaned_data['account_no'])
            if request.is_ajax():
                return JsonResponse(ItemSerializer(item_obj).data)
            return redirect(reverse('item_list'))
    else:
        form = ItemForm(instance=item_obj, request=request)
    if request.is_ajax():
        base_template = '_modal.html'
    else:
        base_template = '_base.html'
    return render(request, 'inventory/item_form.html',
                  {'form': form, 'base_template': base_template, 'scenario': scenario,
                   'item_data': item_obj.other_properties,
                   })


class ItemView(object):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('item_list')

class ItemList(ItemView, ListView):
    pass


class ItemDelete(ItemView, DeleteView):
    pass


def view_inventory_account(request, pk):
    return render(request, 'inventory/home.html')