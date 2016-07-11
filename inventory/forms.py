from django import forms
from django.core.urlresolvers import reverse_lazy
from modeltranslation.forms import TranslationModelForm
from django.utils.translation import ugettext_lazy as _
from ecom.utils.forms import HTML5BootstrapModelForm, KOModelForm
from inventory.models import Unit, InventoryAccount, Item, Company


class UnitForm(HTML5BootstrapModelForm):
    class Meta:
        model = Unit
        exclude = ()


class CompanyForm(HTML5BootstrapModelForm):
    class Meta:
        model = Company
        exclude = ()


class ItemForm(HTML5BootstrapModelForm, KOModelForm, TranslationModelForm):
    account_no = forms.Field(widget=forms.TextInput(), label=_('Inventory Account No.'), required=False)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(ItemForm, self).__init__(*args, **kwargs)

        if self.instance.account:
            self.fields['account_no'].initial = self.instance.account.account_no
        else:
            self.fields['account_no'].initial = InventoryAccount.get_next_account_no()
        if self.instance.id:
            self.fields['account_no'].widget = forms.HiddenInput()
        self.fields['unit'].queryset = Unit.objects.all()
        self.fields['company'].queryset = Company.objects.all()

    def clean_account_no(self):
        if not self.cleaned_data['account_no'].isdigit():
            raise forms.ValidationError("The account no. must be a number.")
        try:
            existing = InventoryAccount.objects.get(account_no=self.cleaned_data['account_no'])
            if self.instance.account.id is not existing.id:
                raise forms.ValidationError("The account no. " + str(
                    self.cleaned_data['account_no']) + " is already in use.")
            return self.cleaned_data['account_no']
        except InventoryAccount.DoesNotExist:
            return self.cleaned_data['account_no']

    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['other_properties', 'account']
        widgets = {
            'unit': forms.Select(attrs={'class': 'selectize', 'data-url': reverse_lazy('unit_add')}),
            'company': forms.Select(attrs={'class': 'selectize', 'data-url': reverse_lazy('company_add')}),
        }
        company_filters = ['unit']

