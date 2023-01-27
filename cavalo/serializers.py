from rest_framework import serializers
from cavalo.cards import card_process
from cavalo.models import Card, Campaign, Users, Bonus


class CardSerializer(serializers.Serializer):
    user_id = serializers.CharField(required=False)
    campaign_id = serializers.CharField()

    class Meta:
        fields = ("campaign_id", "user_id")

    def create(self, validated_data):
        return card_process(user_id=validated_data.get("user_id", None), campaign_id=validated_data["campaign_id"])


