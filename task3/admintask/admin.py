from django.contrib import admin
from .models import Author, Book, Category


# example: @admin.register(class name)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)


# example: admin.site.register(class Name, class Admin Name)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date")
    # filter_horizontal = ("authors",)  # Add a filter for many-to-many fields

    # def display_authors(self, obj):
    #     return ",".join([author.name for author in obj.authors.all()])

    # display_authors.short_description = "Authors"


admin.site.register(Book, BookAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "show_books",
    )
    filter_horizontal = ("books",)

    def show_books(self, obj):
        return ", ".join([book.title for book in obj.books.all()])

    show_books.short_description = "Books"
