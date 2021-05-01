from rest_framework import serializers
from .models import Person


class PersonSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Person

        # or '__all__'
        fields = ['first_name','last_name','gender']







class PersonSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
  

    def create(self, validated_data):

        return Person.objects.create(validated_data)

    def update(self, instance, validated_data):
       # perform object update

       instance.first_name = validated_data.get('first_name', instance.first_name)
       instance.last_name = validated_data.get('last_name', instance.last_name)

       instance.save()
       return instance

