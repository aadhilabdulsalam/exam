from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from products.permissions import IsSuperUserOrAuthenticatedReadOnly
from products.serializers import ProductSerializer
from products.models import Product

class ProductListCreate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUserOrAuthenticatedReadOnly]

    def get(self, request):
        p = Product.objects.all()
        serializer_instance = ProductSerializer(p, many=True)
        return Response(serializer_instance.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer_instance = ProductSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductRetrieveUpdateDelete(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUserOrAuthenticatedReadOnly]

    def get(self, request, pk):
        p = get_object_or_404(Product, id=pk)
        serializer_instance = ProductSerializer(p)
        return Response(serializer_instance.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        p = get_object_or_404(Product, id=pk)
        serializer_instance = ProductSerializer(instance=p, data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        p = get_object_or_404(Product, id=pk)
        serializer_instance = ProductSerializer(instance=p, data=request.data, partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        p = get_object_or_404(Product, id=pk)
        p.delete()
        return Response({"message": "deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
