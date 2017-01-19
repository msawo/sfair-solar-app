from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(User, blank=True, null=True)


# Just adding this new class to be used for later 
class Charge(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.charField(max_length=255)
    percentage = models.PercentField()
    description = models.TextField()

    def __str__(self):
        return self.title
