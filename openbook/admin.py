from django.contrib import admin
from openbook.models import Book,User

# Register your models here.

admin.site.register(Book)




from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = User
admin.site.register(User, CustomUserAdmin)