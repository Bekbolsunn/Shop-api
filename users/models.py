from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ConfirmCode(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    valid_until = models.DateField()

    def __str__(self) -> str:
        return self.code