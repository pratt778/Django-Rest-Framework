from rest_framework import serializers
from .. models import CarList
class SerializeData(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    desc = serializers.CharField()
    active=serializers.BooleanField(read_only=True)
    
    def create(self, validated_data):
        return CarList.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.desc=validated_data.get('desc',instance.desc)
        instance.active=validated_data.get('active',instance.active)
        instance.save()
        return instance
