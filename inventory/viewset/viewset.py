from rest_framework import viewsets

from inventory.models import Item
from inventory.serializer.serializer import ItemSerializer


class ItemViewset(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer