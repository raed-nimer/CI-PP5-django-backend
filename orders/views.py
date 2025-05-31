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
        data = request.data  # <-- this was missing

        cart_items = CartItem.objects.select_related('product')
        .filter(user=request.user)

        if not cart_items.exists():
            return Response(
                {'error': 'Your cart is empty.'},
                status=status.HTTP_400_BAD_REQUEST
                )

        with transaction.atomic():
            total_price = sum(
                item.product.price * item.quantity for item in cart_items
            )

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

            return Response(
                {'message': 'Order placed successfully.',
                    'order_id': order.id},
                status=status.HTTP_201_CREATED)


class ListOrdersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects
        .filter(user=request.user).prefetch_related('order_items__product')

        order_data = []
        for order in orders:
            items = []
            for item in order.order_items.all():
                product = item.product
                items.append({
                    'id': item.id,
                    'product': {
                        'id': product.id,
                        'name': product.name,
                        'price': float(product.price),
                        'image': product.image.url if product.image else None,
                    },
                    'quantity': item.quantity,
                    'price_at_purchase': float(item.price_at_purchase),
                })

            order_data.append({
                'id': order.id,
                'created_at': order.created_at.isoformat(),
                'total_price': float(order.total_price),
                'order_items': items
            })

        return Response(order_data, status=status.HTTP_200_OK)
