from rest_framework import serializers

from .models import Actor


class ActorSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = Actor
        fields = '__all__'
