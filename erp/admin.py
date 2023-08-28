from django.contrib import admin
from .models import Sold_product, Product, Category, UserProfile
# Register your models here.
admin.site.register(Category),
admin.site.register(Product),
admin.site.register(Sold_product),
admin.site.register(UserProfile)

class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ("user", "village", "province", "district", "mobile", "picture", "gender", "bio")
    list_filter = ["user"]
    search_fields = ["user"]
