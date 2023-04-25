from django.db.models import Avg
from rest_framework import serializers
from product.models import Category, Review, Product, Tag
from rest_framework.exceptions import ValidationError


class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)

    class Meta:
        model = Tag
        fields = ("id", "name")


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, required=True)
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("id", "name", "product_count")

    def get_product_count(self, obj):
        return obj.product_set.count()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "text", "stars", "product_id", "created_at")


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)
    description = serializers.CharField(required=False, default="Not description")
    price = serializers.IntegerField()
    category_id = serializers.IntegerField(required=False)  # 100
    is_active = serializers.BooleanField(default=True)
    tag = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    category = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "description",
            "price",
            "is_active",
            "category",
            "category_id",
            "category_display",
            "tag",
        )

    def validate_category_id(self, category_id):  # 100
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError("Category not found!")
        return category_id


class ProductReviewsSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    title = serializers.CharField()
    average_rating = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True)

    def get_average_rating(self, obj):
        return round(obj.reviews.aggregate(avg_rating=Avg("stars"))["avg_rating"], 1)


# class CategoryValidateSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=50, required=True)
#     product_count = serializers.SerializerMethodField()
#
#     def get_product_count(self, obj):
#         return obj.product_set.count()
#
#     def create(self, validated_data):
#         return Category.objects.create(**validated_data)

# class ProductValidateSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=50)
#     description = serializers.CharField(required=False, default="Not description")
#     price = serializers.IntegerField()
#     category_id = serializers.IntegerField(required=False)  # 100
#     is_active = serializers.BooleanField(default=True)
#     tag = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
#
#     def create(self, validated_data):
#         for id, name in Tag.objects.values_list():
#             print(id, name)
#             field = getattr(Product, id)
#             field.set(name)
#
#         return Product.objects.create(**validated_data)
