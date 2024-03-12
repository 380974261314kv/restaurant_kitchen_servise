from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import generic
from django.urls import reverse_lazy

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


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 5
    
    
class DishDetailView(generic.DetailView):
    model = Dish
    
    
class DishCreateView(generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish-list")
    
    
class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish-list")
    
    
class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "restaurant/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 2
    
    
class DishTypeDetailView(generic.DetailView):
    model = DishType
    context_object_name = "dish_type"
    template_name = "restaurant/dish_type_detail.html"
    paginate_by = 5
    
    
class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "restaurant/dish_type_form.html"
    success_url = reverse_lazy("restaurant:dish-type-list")
    
    
class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = "__all__"
    template_name = "restaurant/dish_type_form.html"
    success_url = reverse_lazy("restaurant:dish-type-list")
    
    
class CookListView(generic.ListView):
    model = Cook
    paginate_by = 2
    
    
class CookDetailView(generic.DetailView):
    model = Cook
    
    
class CookCreateView(generic.CreateView):
    model = Cook
    fields = ("username", "first_name", "last_name", "password", "email", "years_of_experience")
    success_url = reverse_lazy("restaurant:cook-list")
    
    
class CookUpdateView(generic.UpdateView):
    model = Cook
    fields = ("username", "first_name", "last_name", "password", "email", "years_of_experience")
    success_url = reverse_lazy("restaurant:cook-list")
