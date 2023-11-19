from django.core.validators import MinValueValidator
from django.db import models


class WodCategoryChoices(models.Choices):
    AMRAP = "AMRAP"
    FOR_TIME = "For Time"
    NOT_FOR_TIME = "Not For Time"
    FOR_LOAD = "For Load"
    EMOM = "EMOM"
    TABATA = "TABATA"


class Movement(models.Model):
    name = models.CharField(unique=True)


class WodMovement(models.Model):
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE)
    repetitions = models.IntegerField(validators=[MinValueValidator(1)], default=1)


class WodRound(models.Model):
    movements = models.ForeignKey(WodMovement, on_delete=models.CASCADE)
    repetitions = models.IntegerField(validators=[MinValueValidator(1)], default=1)


class Wod(models.Model):
    name = models.CharField(max_length=15, blank=True, null=True)
    category = models.CharField(choices=WodCategoryChoices.choices)
    rounds = models.ForeignKey(WodRound, on_delete=models.CASCADE)
