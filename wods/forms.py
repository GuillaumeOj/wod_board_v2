from django.forms.models import ModelForm, inlineformset_factory

from wods.models import RoundInWod, Wod


class RoundInWodForm(ModelForm):
    class Meta:
        model = RoundInWod
        fields = ("repetitions",)


RoundInWodFormset = inlineformset_factory(Wod, RoundInWod, form=RoundInWodForm, extra=1)


class WodForm(ModelForm):
    class Meta:
        model = Wod
        fields = ("name", "category")
