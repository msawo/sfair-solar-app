from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(User, blank=True, null=True)
