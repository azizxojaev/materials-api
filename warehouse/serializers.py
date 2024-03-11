from rest_framework.serializers import ModelSerializer
from .models import *


class ProductsMaterialSerializer(ModelSerializer):
    
    class Meta:
        model = ProductMaterial
        fields = '__all__'

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata['material_name'] = Material.objects.get(id=redata['material']).material_name
        redata['qty'] = redata['quantity']
        # redata['price'] = 
        # redata['warehouse_id'] = Warehouse.objects.get(material__id=redata['material'])
        redata.pop('id')
        redata.pop('quantity')
        redata.pop('material')
        redata.pop('product')
        return redata


class ProductsSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        product_materials = ProductMaterial.objects.filter(product__id=redata['id'])
        redata.pop('id')
        serializer = ProductsMaterialSerializer(instance=product_materials, many=True)
        redata['product_materials'] = serializer.data

        return redata