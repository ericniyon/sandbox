from django.contrib import admin
from registerItem.models import *
from account.models import User

# Register your models here.
admin.site.register(Item)
admin.site.register(Stock)


@admin.register(DivicesCategory)
class DivicesCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
