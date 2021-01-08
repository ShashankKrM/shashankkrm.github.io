from django.db import models
from django.db.models import Model
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Post(models.Model):
    headline = models.CharField(max_length =200)
    sub_heading = models.CharField(max_length = 400)
    thumbnail = models.ImageField(null = True, blank = True, upload_to = "images", default = "placeholder.png")
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default= False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, null = True)
    #slugs

    def __str__(self):
        return self.headline

