from django.db import models
from django.contrib.auth.models import User


class Activation(models.Model):
    code = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
