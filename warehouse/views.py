from rest_framework.views import APIView
from .models import *
from rest_framework import status
from .serializers import *
from rest_framework.response import Response


class ProductsApiView(APIView):

    def get(self, request):
        products_obj = Product.objects.all()

        serializer = ProductsSerializer(instance=products_obj, many=True)

        return Response({'result': serializer.data})