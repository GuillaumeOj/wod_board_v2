from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class WodCategoryChoices(models.Choices):
    AMRAP = "AMRAP"
    FOR_TIME = "For Time"
    NOT_FOR_TIME = "Not For Time"
    FOR_LOAD = "For Load"
    EMOM = "EMOM"
    TABATA = "TABATA"


class Movement(models.Model):
    name = models.CharField(unique=True)


class Round(models.Model):
    movements = models.ManyToManyField(Movement, through="MovementInRound")


class MovementInRound(models.Model):
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    repetitions = models.IntegerField(validators=[MinValueValidator(1)], default=1)


class Wod(models.Model):
    name = models.CharField(max_length=15, blank=True, null=True)
    category = models.CharField(choices=WodCategoryChoices.choices)
    rounds = models.ManyToManyField(Round, through="RoundInWod")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("author"),
        related_name="wods",
        on_delete=models.CASCADE,
        default=None,
    )


class RoundInWod(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    wod = models.ForeignKey(Wod, on_delete=models.CASCADE)
    repetitions = models.IntegerField(validators=[MinValueValidator(1)], default=1)
