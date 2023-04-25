from django.urls import path
from product import views

urlpatterns = [
    # path("products/", views.product_list_view),
    # path("products/<int:id>/", views.product_detail_view),
    # path("category/", views.category_list_view),
    # path("category/<int:id>/", views.category_detail_view),
    # path("reviews/", views.review_list_view),
    # path("reviews/<int:id>/", views.review_detail_view),
    # path("products/reviews/", views.product_reviews_list_view),
    path("products/", views.ProductListView.as_view()),
    path("products/<int:id>/", views.ProductDetailView.as_view()),
    path("categorys/", views.CategoryListView.as_view()),
    path("categorys/<int:id>/", views.CategoryDetailView.as_view()),
    path("reviews/", views.ReviewListView.as_view()),
    path("reviews/<int:id>/", views.ReviewDetailView.as_view()),
    path("tags/", views.TagListView.as_view()),
    path("tags/<int:id>/", views.TagDetailView.as_view()),
    path("product-reviews/", views.ProductReviewListView.as_view()),
]
