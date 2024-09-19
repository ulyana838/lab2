from django.contrib import admin

# Register your models here.
# Импорт модуля admin из библиотеки Django.contrib
from django.contrib import admin
# Импорт модели MyModel из текущего каталога (".")
from .models import MyModel
# Регистрация модели MyModel для административного сайта
admin.site.register(MyModel)