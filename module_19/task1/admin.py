from django.contrib import admin
from .models import *


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'balance', )
    list_filter = ('age', 'balance', )
    search_fields = ('name', )
    list_per_page = 20
    readonly_fields = ('balance', 'password')             # Доступ только для чтения


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'size', 'cost', )            # Отображение полей
    list_filter = ('size', 'cost', )                      # Фильтрация по полям
    search_fields = ('title', )                           # Поиск по полю
    list_per_page = 30                                    # Ограничение кол-ва записей


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date', )
    list_filter = ('title', 'date', )
    search_fields = ('title', )
    list_per_page = 20

admin.site.register(Person)
admin.site.register(Category)

# admin.site.register(Buyer)
# admin.site.register(Game)
