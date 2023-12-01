from typing import Any

from django import forms
from django.forms.formsets import BaseFormSet, formset_factory
from django.forms.models import ModelForm

from wods.models import Movement, Round, Wod


class MovementForm(ModelForm):
    class Meta:
        model = Movement
        fields = ("name",)


class BaseMovementFormset(BaseFormSet):
    def add_fields(self, form: MovementForm, index: int | None) -> None:
        super().add_fields(form, index)
        form.fields["repetitions"] = forms.IntegerField(
            min_value=1, initial=1, required=True
        )


MovementFormset = formset_factory(MovementForm, formset=BaseMovementFormset, extra=1)


class RoundForm(ModelForm):
    class Meta:
        model = Round
        fields = ("repetitions",)

    def __init__(self, *args, wod: Wod, round_index: int | None, **kwargs) -> None:
        self.wod = wod
        if round_index is None:
            round_index = 0
        self.movement_formset = MovementFormset(
            prefix=f"movement_in_round_{round_index}"
        )
        super().__init__(*args, **kwargs)


class BaseRoundFormset(BaseFormSet):
    def get_form_kwargs(self, index: int | None) -> dict[str, Any]:
        form_kwargs = super().get_form_kwargs(index)
        form_kwargs["round_index"] = index
        return form_kwargs


RoundFormset = formset_factory(RoundForm, formset=BaseRoundFormset, extra=1)


class WodForm(ModelForm):
    class Meta:
        model = Wod
        fields = ("name", "category")
