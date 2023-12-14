from django.contrib import admin
from .models import Author, Book, Publisher


# example: @admin.register(class name)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)


# example: admin.site.register(class Name, class Admin Name)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "display_authors", "publisher", "published_date")
    filter_horizontal = ("authors",)  # Add a filter for many-to-many fields

    def display_authors(self, obj):
        return ",".join([author.name for author in obj.authors.all()])

    display_authors.short_description = "Authors"


admin.site.register(Book, BookAdmin)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list = ("name",)
