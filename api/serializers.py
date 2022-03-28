from rest_framework import serializers


class StudentSerializers(serializers.Serializer):
    first_name = serializers.CharField(max_length=200)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
