#!/usr/bin/env python3

from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# Register your models here.

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'date_of_birth',
        'date_of_death',
    )
    fields = [
        'first_name',
        'last_name',
        ('date_of_birth', 'date_of_death',)
    ]


# Register the admin class with the associated Model
admin.site.register(Author, AuthorAdmin)

# Register the admin classes for Book using the decorator
class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'display_genre',
    )
    inlines = [BookInstanceInline]


# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = (
        'book',
        'status',
        'borrower',
        'due_back',
    )

    fieldsets = (
        (
            None, {
                'fields':('book', 'imprint', 'id')
            }
        ),
        ('Availability', {
            'fields':('status', 'due_back', 'borrower')
        })
    )
