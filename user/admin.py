from django.contrib import admin
from .models import SubCategory, Category, Notification
# Register your models here.
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Notification)
