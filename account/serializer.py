from rest_framework import serializers

from .models import achieve

class achieveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = achieve
        fields = ('name', 'stepen', 'photo')