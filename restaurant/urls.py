from django.urls import path
from restaurant.views import (
    index,
    DishListView,
    DishTypeListView,
    CookListView,
)

app_name = "restaurant"

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dish_types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
]
