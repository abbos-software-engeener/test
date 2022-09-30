from rest_framework import serializers

from core.models import Home, Request, Type, HomeType


class HomeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeType
        fields = "__all__"


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = "__all__"


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = "__all__"
