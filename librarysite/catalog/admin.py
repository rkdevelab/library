from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)




# Define the admin class
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    #zeigt auf der admin seite diese infos an:
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death') #zeigt auf der admin seite diese infos an
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')] #verändert anordnung auf admin seite bei change author




class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0 #use if you dont want three placeholders for new book instances 
# add inlines = [BooksInstanceInline] in @admin.register(Book)
# for each book the bottom of the change site you should now see the book instances relating to this book

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline] 




# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','id','status', 'borrower', 'due_back')

    # list_filter fügt auf admin seite auswahlmöglichkeit hinzu welche objekte angezeigt werden sollen
    list_filter = ('status', 'due_back')
    
    # adds sections on the admin change site, None and Availability are headlines
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'borrower', 'due_back')
        }),
    )




# we can't directly specify the genre field in Books list_display because it is a ManyToManyField 
# that's why a function is defined in models.py Book

