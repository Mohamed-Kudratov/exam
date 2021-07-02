from django.contrib import admin

from django.contrib import admin

from user.models import UserModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'salary', 'created_at']
    search_fields =['name', 'created_at']