from django.contrib import admin
from product.models import Product, Category, Review, Tag

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Tag)
