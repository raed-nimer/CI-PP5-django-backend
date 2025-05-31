from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CartItem
from product.models import Product


def serialize_cart_item(cart_item):
    return {
        'id': cart_item.id,
        'product': {
            'id': cart_item.product.id,
            'name': cart_item.product.name,
            'price': str(cart_item.product.price),
            'image': (
                cart_item.product.image.url
                if cart_item.product.image else None
            ),
        },
        'quantity': cart_item.quantity
    }


class CartItemsView(APIView):
    def get(self, request):
        if request.user and request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user)
            data = [serialize_cart_item(item) for item in cart_items]
            return Response(data)
        else:
            return Response([])  # Guest cart handled in frontend


class AddToCartView(APIView):
    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        if not product_id:
            return Response(
                {"error": "Product ID is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Invalid Product ID."},
                status=status.HTTP_404_NOT_FOUND
            )

        if request.user and request.user.is_authenticated:
            cart_item, created = CartItem.objects.get_or_create(
                user=request.user,
                product=product
            )
            if not created:
                cart_item.quantity += int(quantity)
            else:
                cart_item.quantity = int(quantity)
            cart_item.save()
            return Response(
                serialize_cart_item(cart_item),
                status=status.HTTP_201_CREATED
            )
        else:
            # Guest user - frontend will handle
            return Response({
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "price": str(product.price),
                    "image": (
                        product.image.url
                        if product.image else None
                    ),
                },
                "quantity": quantity
            }, status=status.HTTP_201_CREATED)


class UpdateCartItemView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        try:
            cart_item = CartItem.objects.get(id=pk, user=request.user)
        except CartItem.DoesNotExist:
            return Response(
                {'error': 'Item not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        quantity = request.data.get('quantity')
        if quantity is None:
            return Response(
                {'error': 'Quantity is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            quantity = int(quantity)
            if quantity < 1:
                return Response(
                    {'error': 'Quantity must be at least 1'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except ValueError:
            return Response(
                {'error': 'Quantity must be an integer'},
                status=status.HTTP_400_BAD_REQUEST
            )

        cart_item.quantity = quantity
        cart_item.save()
        return Response(serialize_cart_item(cart_item))


class DeleteCartItemView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        try:
            cart_item = CartItem.objects.get(id=pk, user=request.user)
            cart_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            return Response(
                {'error': 'Item not found'},
                status=status.HTTP_404_NOT_FOUND
            )
