# from pprint import pprint
#
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from rest_framework import generics  # status

from product.models import (
    Category,
    Product,
    Review,
    Tag,
)
from product.serializers import (
    ProductSerializer,
    CategorySerializer,
    ReviewSerializer,
    ProductReviewsSerializer,
    TagSerializer,
    # ProductValidateSerializer,
    # CategoryValidateSerializer,
)


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ReviewListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class TagListView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ProductReviewListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductReviewsSerializer


# @api_view(["GET", "POST"])
# def product_list_view(request):
#     if request.method == "GET":
#         product = Product.objects.all()
#         serializer = ProductSerializer(instance=product, many=True)
#         return Response(data=serializer.data)
#     elif request.method == "POST":
#         serializer = ProductSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(
#                 data={"errors": serializer.errors},
#                 status=status.HTTP_406_NOT_ACCEPTABLE,
#             )
#         pprint(serializer.validated_data)
#         title = serializer.validated_data.get("title")
#         description = serializer.validated_data.get("description")
#         price = serializer.validated_data.get("price")
#         category_id = serializer.validated_data.get("category_id")
#         tag = serializer.validated_data.get("tag")
#         new_product = Product.objects.create(
#             title=title, description=description, price=price, category_id=category_id, tag=tag
#         )
#         new_product.tag.set(tag)
#         new_product.save()
#         return Response(data=ProductSerializer(new_product).data)
#
#
# @api_view(["GET", "PUT", "DELETE"])
# def product_detail_view(request, id):
#     try:
#         product = Product.objects.get(id=id)
#     except Product.DoesNotExist:
#         return Response(
#             status=status.HTTP_404_NOT_FOUND, data={"error": "Object not found maaan!"}
#         )
#     if request.method == "GET":
#         serializer = ProductSerializer(product)
#         return Response(data=serializer.data)
#     elif request.method == "DELETE":
#         product.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT, data={"complete": "Object removed!"}
#         )
#     elif request.method == "PUT":
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         product.title = serializer.validated_data.get("title")
#         product.description = serializer.validated_data.get("description")
#         product.price = serializer.validated_data.get("price")
#         product.category_id = serializer.validated_data.get("category_id")
#         product.save()
#         return Response(data=ProductSerializer(product).data)


# @api_view(["GET", "POST"])
# def category_list_view(request):
#     if request.method == "GET":
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many=True)
#         return Response(data=serializer.data)
#     elif request.method == "POST":
#         serializer = CategorySerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(
#                 data={"errors": serializer.errors},
#                 status=status.HTTP_406_NOT_ACCEPTABLE,
#             )
#         name = request.data.get("name")
#         new_category = Category.objects.create(name=name)
#         return Response(data=CategorySerializer(new_category).data)
#
#
# @api_view(["GET", "DELETE", "PUT"])
# def category_detail_view(request, id):
#     try:
#         category = Category.objects.get(id=id)
#     except Category.DoesNotExist:
#         return Response(
#             status=status.HTTP_404_NOT_FOUND, data={"error": "Object not found maaan!"}
#         )
#     if request.method == "GET":
#         serializer = CategorySerializer(category)
#         return Response(data=serializer.data)
#     elif request.method == "DELETE":
#         category.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT, data={"complete": "Object removed!"}
#         )
#     elif request.method == "PUT":
#         category.name = request.data.get("name")
#         category.save()
#         return Response(data=CategorySerializer(category).data)


# @api_view(["GET", "POST"])
# def review_list_view(request):
#     if request.method == "GET":
#         review = Review.objects.all()
#         serializer = ReviewSerializer(review, many=True)
#         return Response(data=serializer.data)
#     elif request.method == "POST":
#         stars = request.data.get("stars")
#         text = request.data.get("text")
#         product_id = request.data.get("product_id")
#         new_review = Review.objects.create(
#             text=text, product_id=product_id, stars=stars
#         )
#         return Response(data=ReviewSerializer(new_review).data)
#
#
# @api_view(["GET", "PUT", "DELETE"])
# def review_detail_view(request, id):
#     try:
#         review = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(
#             status=status.HTTP_404_NOT_FOUND, data={"error": "Object not found maaan!"}
#         )
#     if request.method == "GET":
#         serializer = ReviewSerializer(review)
#         return Response(data=serializer.data)
#     elif request.method == "DELETE":
#         review.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT, data={"complete": "Object removed!"}
#         )
#     elif request.method == "PUT":
#         review.stars = request.data.get("stars")
#         review.text = request.data.get("text")
#         review.product_id = request.data.get("product_id")
#         review.save()
#         return Response(data=ReviewSerializer(review).data)
#
# @api_view(["GET"])
# def product_reviews_list_view(request):
#     product = Product.objects.all()
#     serializer = ProductReviewsSerializer(product, many=True)
#     return Response(data=serializer.data)
