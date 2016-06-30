from django.conf.urls import url, include
from inventory import views as inventory_views
from rest_framework import routers

from inventory.viewset.viewset import ItemViewset

app_name="inventory"

router = routers.DefaultRouter()
router.register(r'item', ItemViewset)



urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^$', inventory_views.home, name="home"),

    url(r'^item/$', inventory_views.ItemList.as_view(), name='item_list'),
    url(r'^item/add/$', inventory_views.item, name='item_add'),
    url(r'^item/(?P<pk>[0-9]+)/$', inventory_views.item, name='item_edit'),
    # url(r'^item/search/$', inventory_views.item_search, name='search-item'),
    url(r'^item/delete/(?P<pk>\d+)/$', inventory_views.ItemDelete.as_view(), name='item_delete'),
    url(r'^unit/$', inventory_views.UnitListView.as_view(), name='unit_list'),
    url(r'^unit/add$', inventory_views.UnitCreate.as_view(), name='unit_add'),
    url(r'^unit/edit/(?P<pk>\d+)/$', inventory_views.UnitUpdate.as_view(), name='unit_edit'),
    url(r'^unit/delete/(?P<pk>\d+)/$', inventory_views.UnitDelete.as_view(), name='unit_delete'),
]
