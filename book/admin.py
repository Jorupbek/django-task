from django.contrib import admin

from book.models import Book, Review, BookMark


@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'author', 'publication_date')
    list_display_links = ('title', 'genre')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Review)
admin.site.register(BookMark)
