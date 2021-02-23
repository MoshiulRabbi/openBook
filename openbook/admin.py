from django.contrib import admin
from openbook.models import Book,User,lend

# Register your models here.

admin.site.register(Book)
admin.site.register(lend)




from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = User
admin.site.register(User, CustomUserAdmin)