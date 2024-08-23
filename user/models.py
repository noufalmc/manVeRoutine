from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Notification(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    device_id = models.CharField(max_length=256)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    login_at = models.DateTimeField(auto_now_add=True)
    logout_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    title = models.TextField()
    description = models.TextField()
    image_field = models.ImageField(upload_to="category")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "---" + self.description


class SubCategory(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    title = models.TextField()
    parent = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class UserScape(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    short_description = models.TextField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
