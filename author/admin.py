from django.contrib import admin

from author.models import Author, Genre


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)
    prepopulated_fields = {"slug": ("name",)}
