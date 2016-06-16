from ecom.utils.forms import HTML5BootstrapModelForm
from inventory.models import Unit


class UnitForm(HTML5BootstrapModelForm):
    class Meta:
        model = Unit
        exclude = ()
