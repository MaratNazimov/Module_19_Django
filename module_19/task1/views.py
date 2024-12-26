from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import UserRegister    #, AuthorizationsForm
from django.core.paginator import Paginator

def news(request):
    news_all = News.objects.all().order_by('-date')    # order_by('-date') Сортировка по дате
    paginator = Paginator(news_all, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'news': page_obj}
    return render(request, 'fourth_task/news.html', context)

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

# def authorization_user(request):
#     users = Buyer.objects.all()
#     list_name = [user.name for user in users]
#     list_password = [user.password for user in users]
#     if request.method == "POST":
#         form = AuthorizationsForm(request.POST)
#         username = request.GET.get("username")
#         password = request.GET.get("password")
#         print(username)
#         print(password)
#         print(list_name)
#         print(list_password)
#
#
#     else:
#         return HttpResponse(f"Приветствуем, {username}!")


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
