from rest_framework import serializers

from inventory.models import Item, Unit, Company, Category


class UnitSerializer(serializers.ModelSerializer):
    convertible_units = serializers.SerializerMethodField()

    def get_convertible_units(self, obj):
        return obj.convertibles()

    class Meta:
        model = Unit


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class ItemSerializer(serializers.ModelSerializer):
    unit = UnitSerializer()
    company = CompanySerializer()
    category = CategorySerializer()
    name = serializers.ReadOnlyField(source='__unicode__')

    class Meta:
        model = Item
