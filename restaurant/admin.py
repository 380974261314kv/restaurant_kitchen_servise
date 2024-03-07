from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from restaurant.models import Cook, Dish, DishType


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "dish_type")
    
    
@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    
    
@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional info",
            {
                "fields": ("years_of_experience",)
            }
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "years_of_experience",
                )
            }
        ),
    )
