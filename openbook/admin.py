from django.contrib import admin
from openbook.models import Book,User,lend,review

# Register your models here.

admin.site.register(Book)
admin.site.register(lend)
admin.site.register(review)




from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = User
admin.site.register(User, CustomUserAdmin)