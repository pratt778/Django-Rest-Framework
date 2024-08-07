from rest_framework import serializers
from .. models import CarList,ShowroomList
from decimal import Decimal

# def alphanum(value):
#     if not str(value).isalnum():
#         raise serializers.ValidationError("License no should be alphanumeric")
#     return value

class SerializeData(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField()
    # desc = serializers.CharField()
    # active = serializers.BooleanField(read_only=True)
    # price = serializers.DecimalField(max_digits=9, decimal_places=2)
    # license_no = serializers.CharField(validators=[alphanum])

    #custom fields
    discounted_price = serializers.SerializerMethodField()
    tax_price = serializers.SerializerMethodField()
    class Meta:
        model = CarList
        fields = "__all__"
        read_only_fields=['id','active']
        # fields= ['name','desc','price']
    
    def get_tax_price(self,object):
        # tax=Decimal('0.13')
        # t_price = object.price*(1+tax)
        t_price = object.price+(Decimal(13/100)*object.price)
        return t_price
    
    def get_discounted_price(self,object):
        d_price= object.price - 5000 
        return d_price

    def create(self, validated_data):
        return CarList.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.desc=validated_data.get('desc',instance.desc)
        instance.active=validated_data.get('active',instance.active)
        instance.price=validated_data.get('price',instance.price)
        instance.license_no = validated_data.get('license_no',instance.license_no)
        instance.save()
        return instance
    
    def validate_price(self,value):
        if(value<=20000):
            raise serializers.ValidationError("Price must be greater than 20000")
        return value

    def validate(self,data):
        if data['name']==data['desc']:
            raise serializers.ValidationError('Name and description must be different')
        return data
    

class ShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowroomList
        fields="__all__"
    # def create(self,validated_data):
    #     return ShowroomList.objects.create(**validated_data)