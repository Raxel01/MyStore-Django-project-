from rest_framework import serializers
from .models import *
from decimal import Decimal

# We can use serializers.ModelSerializer
# insted of <serializers.Serializer>

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Collection
        fields = ['id']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
       model = Product
       fields =  ['id', 'title', 'unit_price', 'price_with_tax', 'collection', ]
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    collection = serializers.PrimaryKeyRelatedField( queryset=Collection.objects.all())
    # collection_id = serializers.SerializerMethodField(method_name='getcollectionname');

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
    # def getcollectionname(self, product: Product):
    #     return product.collection.id
    
    