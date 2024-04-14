from django.forms import ModelForm
from optimizationapp.models import Metamaterial

class MetamaterialForm(ModelForm):

    class Meta:
        model=Metamaterial
        fields = ["Wm", "W0m", "dm", "tm", "rows",
                  "Xa","Ya", "gain", "vswr", "bandwidth"]

        