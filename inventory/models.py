from django.core.urlresolvers import reverse_lazy
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Company(models.Model):
    name = models.CharField(max_length=256)


class Category(MPTTModel):
    name = models.CharField(max_length=256, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)


class Unit(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10, blank=True, null=True)

    def get_base_conversions(self, exclude=None):
        return self.base_conversions.all()

    def get_conversions(self, exclude=None):
        return self.conversions.all()

    def get_all_conversions(self, exclude=[]):

        base_conversions = UnitConversion.objects.filter(base_unit=self).exclude(pk__in=exclude)
        conversions = UnitConversion.objects.filter(unit_to_convert=self).exclude(pk__in=exclude)
        ret = []
        for base_conversion in base_conversions:
            ret.append(base_conversion)
        for conversion in conversions:
            conversion.multiple = 1 / conversion.multiple
            ret.append(conversion)
        return ret

        qs = UnitConversion.objects.filter(base_unit=self).extra(
            select={'multiple': '1 / multiple'}) | UnitConversion.objects.filter(
            unit_to_convert=self)
        return qs.exclude(pk__in=exclude)

    def convertibles(self):
        def find_convertibles(data, exclude, mul, base_unit=None):
            # print ''
            if not base_unit:
                base_unit = self
            # print 'Convertible for ' + str(base_unit)
            # print 'Passed multiple is ' + str(mul)
            if base_unit.id not in data.keys():
                data[base_unit.id] = mul
                # print data
                # print 'Exclude: ' + str(exclude)
                # print 'Conversions: ' + str(base_unit.get_all_conversions(exclude))
                for conversion in base_unit.get_all_conversions(exclude):
                    exclude.append(conversion.pk)
                    unit = conversion.get_another_unit(base_unit.id)
                    # print '\nConverting to ' + str(unit) + ' with multiple ' + str(conversion.multiple * mul)
                    for key, val in find_convertibles(data, exclude, conversion.multiple * mul, unit).items():
                        if not key in data.keys():
                            # print 'writing: ' + str(key) + ' : ' + str(val)
                            data[key] = val * conversion.multiple
            return data

        all_convertibles = find_convertibles({}, [], 1)
        all_convertibles.pop(self.id, None)
        return all_convertibles

        # for conversion in self.get_conversions():
        #     if conversion.base_unit_id not in data.keys():
        #         for key, val in conversion.base_unit.convertibles(data).items():
        #             data[key] = val / conversion.multiple
        #     data[conversion.base_unit_id] = 1 / conversion.multiple
        # return data

    def __unicode__(self):
        return self.name


class UnitConversion(models.Model):
    base_unit = models.ForeignKey(Unit, null=True, related_name='base_conversions')
    unit_to_convert = models.ForeignKey(Unit, null=True, related_name='conversions')
    multiple = models.FloatField()

    def get_another_unit(self, unit_id):
        if unit_id == self.base_unit_id:
            return self.unit_to_convert
        return self.base_unit

    def __unicode__(self):
        return self.base_unit.name + ' - ' + self.unit_to_convert.name + ' : ' + str(self.multiple)


class InventoryAccount(models.Model):
    name = models.CharField(max_length=100)
    account_no = models.PositiveIntegerField()
    current_balance = models.FloatField(default=0)

    def __str__(self):
        return str(self.account_no) + ' [' + self.name + ']'

    def get_absolute_url(self):
        # return '/inventory_account/' + str(self.id)
        return reverse_lazy('view_inventory_account', kwargs={'pk': self.pk})

    @staticmethod
    def get_next_account_no():
        from django.db.models import Max

        max_voucher_no = InventoryAccount.objects.all().aggregate(Max('account_no'))['account_no__max']
        if max_voucher_no:
            return max_voucher_no + 1
        else:
            return 1



class Item(models.Model):
    name = models.CharField(max_length=256)
    rate = models.FloatField(null=True)
    company = models.ForeignKey(Company, null=True)
    account = models.OneToOneField(InventoryAccount, related_name='item', null=True)
    unit = models.ForeignKey(Unit)
    category = models.ForeignKey(Category, related_name='item_category', null=True, blank=True)

    def __str__(self):
        return str(self.name)


class OtherProperties(models.Model):
    item = models.ForeignKey(Item, related_name='properties')
    name = models.CharField(max_length=256)
    value = models.CharField(max_length=256)


class ItemImages(models.Model):
    item = models.ForeignKey(Item, related_name='images')
    file = models.ImageField(upload_to='items')


class Inventory(models.Model):
    item = models.ForeignKey(Item, related_name='inventory')
    stock = models.FloatField(null=True)