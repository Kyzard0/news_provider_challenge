from django.contrib import admin

from .models import Author, Article


@admin.register(Author)
class Authors(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name']
    ordering = ('name',)


@admin.register(Article)
class Articles(admin.ModelAdmin):
    list_display = ['title', 'author', ]
    search_fields = ['title']
    ordering = ('title',)
