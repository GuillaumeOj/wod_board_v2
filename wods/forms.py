from django.forms.models import ModelForm

from wods.models import Wod


class WodForm(ModelForm):
    class Meta:
        model = Wod
        fields = ("name", "category")
