from rest_framework import serializers

from product.models import Product, Category, Review


class ProductSerializer(serializers.Serializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'category')


class ProductRetrieveSerializer(serializers.Serializer):

    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.Serializer):

    class Meta:
        model = Category
        fields = ('id', 'name')


class CategoryRetrieveSerializer(serializers.Serializer):

    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer(serializers.Serializer):

    class Meta:
        model = Review
        fields = ('product', 'text')


class ReviewRetrieveSerializer(serializers.Serializer):

    class Meta:
        model = Review
        fields = '__all__'
