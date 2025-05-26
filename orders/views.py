from .models import Order, OrderItem 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, permissions
from cart.models import CartItem
from django.db import transaction
# Create your views here.

class PlaceOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart_items = CartItem.objects.select_related('product').filter(user=request.user)

        if not cart_items.exists():
            return Response({'error': 'Your cart is empty.'}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            total_price = sum(item.product.price * item.quantity for item in cart_items)

        order = Order.objects.create(
            user=request.user,
            total_price=total_price,
            first_name=data.get('firstName'),
            last_name=data.get('lastName'),
            email=data.get('email'),
            address=data.get('address'),
            country=data.get('country'),
            state=data.get('state'),
            zip=data.get('zip'),
            payment_method=data.get('paymentMethod'),
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price_at_purchase=item.product.price
            )

        cart_items.delete()

        return Response({'message': 'Order placed successfully.', 'order_id': order.id}, status=status.HTTP_201_CREATED)
