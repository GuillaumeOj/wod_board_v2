from rest_framework import serializers

from users.serializers import UserSerializer
from wods.models import Movement, MovementInRound, Round, Wod


class MovementInRoundSerializer(serializers.ModelSerializer):
    movement = serializers.SerializerMethodField()

    class Meta:
        model = MovementInRound
        fields = ("id", "movement", "repetitions")

    def create(self, validated_data):
        return super().create(validated_data)

    def get_movement(self, movement_in_round):
        return movement_in_round.movement


class RoundSerializer(serializers.ModelSerializer):
    movements = MovementInRoundSerializer(many=True)

    class Meta:
        model = Round
        fields = ("id", "repetitions", "movements")
        depth = 1


class WodSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    rounds = RoundSerializer(many=True)

    class Meta:
        model = Wod
        fields = ("id", "name", "category", "rounds", "user")
        depth = 1

    def create(self, validated_data):
        user = self.context["request"].user
        rounds_data = validated_data.pop("rounds")
        wod = Wod.objects.create(user=user, **validated_data)

        for round_data in rounds_data:
            movements_data = round_data.pop("movements")
            round = Round.objects.create(wod=wod, **round_data)
            for movement_data in movements_data:
                __import__("pdb").set_trace()
                movement_name = movement_data.pop("name")
                movement = Movement.objects.get_or_create(name=movement_name)
                MovementInRound.objects.create(
                    round=round, movement=movement, **movement_data
                )

        return wod

    def get_user(self, wod):
        return UserSerializer(wod.user).data
