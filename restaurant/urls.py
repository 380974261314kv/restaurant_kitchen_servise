from django.urls import path
from restaurant.views import (
    index,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishTypeListView,
    DishTypeDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookUpdateView,
)

app_name = "restaurant"

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/update/<int:pk>/", DishUpdateView.as_view(), name="dish-update"),
    path("dish_types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish_types/<int:pk>/", DishTypeDetailView.as_view(), name="dish-type-detail"),
    path("dish_types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish_types/update/<int:pk>/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/update/<int:pk>/", CookUpdateView.as_view(), name="cook-update"),
]
