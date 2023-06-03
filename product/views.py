from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from product.models import Product, Review, Category
from product.serializers import ProductSerializer, CategorySerializer, ReviewSerializer, CategoryRetrieveSerializer, \
    ProductRetrieveSerializer, ReviewRetrieveSerializer


@api_view(['GET'])
def products_api_view(request):
    products = Product.objects.all()

    data = ProductSerializer(products, many=True).data

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def products_retrieve_api_view(request, **kwargs):
    product = Product.objects.get(id=kwargs['id'])

    data = ProductRetrieveSerializer(Product, many=False).data

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def products_categories_api_view(request):
    categories = Category.objects.all()

    data = CategorySerializer(categories, many=True).data

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def categories_retrieve_api_view(request, **kwargs):
    category = Category.objects.get(id=kwargs['id'])

    data = CategoryRetrieveSerializer(category, many=False).data

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_review_api_view(request):
    reviews = Review.objects.all()

    data = ReviewSerializer(reviews, many=True).data

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_retrieve_api_view(request, **kwargs):
    review = Review.objects.get(id=kwargs['id'])

    data = ReviewRetrieveSerializer(review, many=False).data

    return Response(data=data, status=status.HTTP_200_OK)
