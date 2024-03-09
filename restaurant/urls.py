from django.urls import path
from restaurant.views import (
    index,
    DishListView,
    DishDetailView,
    DishTypeListView,
    DishTypeDetailView,
    CookListView,
    CookDetailView,
)

app_name = "restaurant"

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish_types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish_types/<int:pk>/", DishTypeDetailView.as_view(), name="dish-type-detail"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
]
