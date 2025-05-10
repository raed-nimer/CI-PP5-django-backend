from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# @api_view(['GET'])
class ProductListView(APIView):
    authentication_classes = []  # Optional: explicitly disable auth
    permission_classes = []      # No permissions required

    def get(self, request):
        products = Product.objects.all()
        data = [
            {
                'id': p.id,
                'name': p.name,
                'description': p.description,
                'category': p.category.name,
                'image': str(p.image),
                'price': str(p.price)
            } for p in products
        ]
        return Response(data)    
# blogs = Blog.objects.all()
# serializer = BlogSerializer(blogs, many=True)
# return Response(serializer.data)
