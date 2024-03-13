from rest_framework.views import APIView
from .models import *
from rest_framework import status
from .serializers import *
from rest_framework.response import Response


class ProductsApiView(APIView):

    def get(self, request):
        products_obj = Product.objects.all()

        serializer = ProductsSerializer(instance=products_obj, many=True)

        warehouses = {}
        for i in serializer.data:
            for p in i['product_materials']:
                if warehouses.get(f"{p['warehouse_id']}") == None:
                    warehouses[f"{p['warehouse_id']}"] = p['qty']
                else:
                    warehouses[f"{p['warehouse_id']}"] += p['qty']
                remainder = Warehouse.objects.get(id=p['warehouse_id']).remainder
                qty = warehouses[f"{p['warehouse_id']}"]
                if qty > remainder:
                    p['warehouse_id'] = None
                    p['price'] = None

        return Response({'result': serializer.data})