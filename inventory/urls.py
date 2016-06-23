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
    url(r'^item/(?P<pk>[-\w]+)/$', inventory_views.ItemDetailView.as_view(), name='item_detail'),
    url(r'^unit/$', inventory_views.UnitListView.as_view(), name='unit_list'),
    url(r'^unit/add$', inventory_views.UnitCreate.as_view(), name='unit_add'),
    url(r'^unit/edit/(?P<pk>\d+)/$', inventory_views.UnitUpdate.as_view(), name='unit_edit'),
    url(r'^unit/delete/(?P<pk>\d+)/$', inventory_views.UnitDelete.as_view(), name='unit_delete'),
]
