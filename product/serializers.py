from rest_framework import serializers

from product.models import Product, Category, Review


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'category')


class ProductRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')


class CategoryRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('product', 'text')


class ReviewRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
