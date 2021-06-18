from rest_framework import serializers
from .models import Person, Car, PersonsProfile, Laptop





class PersonProfileSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = PersonsProfile
        fields = ['bio','phone']




class LaptopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Laptop
        fields = ['name','price']

class PersonSerializers(serializers.ModelSerializer):
    # cars_of_user = CarSerializer(many=True, read_only=True)
    # profile = PersonProfileSerializer(many=True, read_only=True)
    # profile = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    # laptops = LaptopSerializer(many=True)

    class Meta:
        model = Person
        fields = ['first_name','last_name','email','gender',]
      
class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['name','price','owner']
        depth = True


    
    # def create(self, validated_data):
    #     laptop_data = validated_data.pop('laptops')
    #     owner = Person.objects.create(**validated_data)
    #     for data in laptop_data:
    #         Laptop.objects.create(owner=owner, **data)
    #     return owner

    






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



class OneToOnePersonSeializer(serializers.ModelSerializer):
    user = PersonSerializers()


    class Meta:
        model = PersonsProfile
        fields = ('user','bio','phone_no')

    # def create(self, validated_data):
    #     data = validated_data.pop('persons_data')
    #     user = PersonsProfile.objects.create(**validated_data)
    #     Person.objects.create(user=user, **data)
    #     return user