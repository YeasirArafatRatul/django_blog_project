from rest_framework import serializers
from .models import KeyValue

# converting to json and validation for passed data+

class KeyValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyValue
        fields = ['key', 'value', 'timestamp' ]