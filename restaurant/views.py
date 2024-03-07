from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from restaurant.models import Cook, Dish, DishType


def index(request: HttpRequest) -> HttpResponse:
    
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()
    
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
        "num_visits": num_visits
    }
  
    return render(request, "restaurant/index.html", context=context)
