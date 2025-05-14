from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import ContactFormResponse

# Create your views here.
# Signup View
class IndexView(APIView):
    def get(self, request):
        return Response({'message': 'Welcome to the Powerhouse API!'})

class ContactFormResponseView(APIView):
    def get(self, request):
        return Response({'message': 'Contact Form Response API!'})
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        subject = request.data.get('subject')
        description = request.data.get('description')

        # Save the data to the database
        contact_form_response = ContactFormResponse(
            name=name,
            email=email,
            subject=subject,
            description=description
        )
        contact_form_response.save()

        return Response({'message': 'Contact form response saved successfully!'})