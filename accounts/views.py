from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
# Create your views here.
# Signup View


class RegisterView(APIView):
    def post(self, request):
        try:
            # name = request.data.get('name')
            # print request.data
            first_name = request.data.get('firstName')
            print("request Hit")
            print(first_name)
            last_name = request.data.get('lastName')
            # username = request.data.get('username')
            email = request.data.get('email')
            password = request.data.get('password')

            if not email or not password:
                return Response(
                        {'error': 'Username, email and password required'},
                        status=400
                        )

            if User.objects.filter(email=email).exists():
                return Response(
                        {'error': 'Account already exists'}, status=400)

            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=email,
                email=email,
                password=make_password(password)
            )

            refresh = RefreshToken.for_user(user)
            return Response({
                'status': 'success',
                'message': 'User created successfully',
                'user': {
                    'id': user.id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                },
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        except Exception as e:
            print("Error in RegisterView:", e)
            return Response({'error': 'An error occurred'}, status=500)
# Login View


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            print("Email and password required")
            return Response(
                    {'error': 'Username and password required'}, status=400)

        user = User.objects.filter(email=email).first()

        if user is None or not user.check_password(password):
            print("Invalid credentials")
            print(user)
            return Response({'error': 'Invalid credentials'}, status=400)

        refresh = RefreshToken.for_user(user)
        return Response({
            'status': 'success',
            'message': 'Login successful',
            'user': {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
            },
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


# Get and Update Profile View
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    # GET /profile
    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        })

    # POST /profile
    def post(self, request):
        user = request.user
        first_name = request.data.get('first_name', user.first_name)
        last_name = request.data.get('last_name', user.last_name)

        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return Response({
            'status': 'success',
            'message': 'Profile updated successfully',
            'user': {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
            }
        })
