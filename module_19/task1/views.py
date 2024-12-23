from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import UserRegister

def bd_buyer(request):
    buyer_all = Buyer.objects.all()
    context = {
        'buyer_all': buyer_all,
    }
    return render(request, 'fifth_task/bd_buyer.html', context)

def main_page(request):
    title = 'Главная страница'
    context  = {
        'title': title,
    }
    return render(request, 'fourth_task/main_page.html', context)

def shop(request):
    title = 'Магазин'
    game_all = Game.objects.all()
    context = {
        'title': title,
        'content': game_all,
    }
    return render(request, 'fourth_task/shop.html', context)

def basket(request):
    title = 'Корзина'
    context = {
        'title': title,
    }
    return render(request, 'fourth_task/basket.html', context)

def base_menu(request):
    title = 'base Menu'
    context = {
        'title': title
    }
    return render(request, 'fourth_task/base_menu.html', context)


def form_register(request):
    users = Buyer.objects.all()
    list_user = [user.name for user in users]

    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]
            subscribe = form.cleaned_data["subscribe"]

            for i in list_user:
                if i == username:
                    error = "Пользователь уже существует"
                    return render(request, "fifth_task/registration_page.html",
                                  {"error": error})
            if int(age) < 18:
                error = "Вы должны быть старше 18"
                return render(request, "fifth_task/registration_page.html",
                              {"error": error})
            if password != repeat_password:
                error = "Пароли не совпадают"
                return render(request, "fifth_task/registration_page.html",
                              {"error": error})
            if subscribe == False:
                error = "Вы не подтвердили согласие на обработку персональных данных"
                return render(request, "fifth_task/registration_page.html",
                              {"error": error})
            else:
                Buyer.objects.create(name = username,
                                     password = password,
                                     balance = 0,
                                     age = age,
                                     subscribe = subscribe)
                return HttpResponse(f"Приветствуем, {username}!")
    else:
        form = UserRegister()
    return render(request, "fifth_task/registration_page.html", {'form': form})

# def sign_up_by_html(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         repeat_password = request.POST.get("repeat_password")
#         age = request.POST.get("age")
#         subscribe = request.POST.get("subscribe")
#
#         for i in users:
#             if i == username:
#                 error = "Пользователь уже существует"
#                 return render(request, "fifth_task/registration_page.html",
#                               {"error": error})
#         if int(age) < 18:
#             error = "Вы должны быть старше 18"
#             return render(request, "fifth_task/registration_page.html",
#                           {"error": error})
#         if password != repeat_password:
#             error = "Пароли не совпадают"
#             return render(request, "fifth_task/registration_page.html",
#                           {"error": error})
#         if subscribe != 'on':
#             error = "Вы не подтвердили согласие на обработку персональных данных"
#             return render(request, "fifth_task/registration_page.html",
#                           {"error": error})
#         else:
#             return HttpResponse(f"Приветствуем, {username}!")
#     return render(request, "fifth_task/registration_page.html")