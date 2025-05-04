from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
# Signup View
class IndexView(APIView):
    def get(self, request):
        return Response({'message': 'Welcome to the Powerhouse API!'})