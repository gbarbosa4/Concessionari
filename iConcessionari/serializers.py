from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Factory, Client, Car

class FactorySerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='factory-detail')
    user = CharField(read_only=True)
    class Meta:
        model = Factory
        fields = ('url','name','country','city','address','telephone','production','stock')

class ClientSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='client-detail')
    user = CharField(read_only=True)
    class Meta:
        model = Client
        fields =('url','name','last_name','email','dni','telephone','country','city','address')

class CarSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='car-detail')
    factory = HyperlinkedRelatedField(view_name='factory-detail')
    client = HyperlinkedRelatedField(view_name='client-detail')
    user = CharField(read_only=True)
    class Meta:
        model = Car
        fields = ('url','brand','model','price', 'client', 'factory')
