from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, null=True)
    tag = models.ManyToManyField(to=Tag, blank=True)

    def __str__(self) -> str:
        return self.title

    def get_breed(self):
        return self.title + ' belongs to ' + self.description + ' breed.'

    @property
    def category_display(self):
        return self.category.name


STARS = ((i, "*" * i) for i in range(1, 6))


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, related_name="reviews"
    )
    stars = models.IntegerField(choices=STARS, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.id, self.text} под {self.product}"
