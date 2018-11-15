from django.contrib import admin
from .models import Author, Note
# Register your models here.

class AuthorAdmin( admin.ModelAdmin):
    list_display = ( "user", "dob" )

class NoteAdmin( admin.ModelAdmin):
    list_display = ( "title", "last_modified")
    list_filter = ("last_modified", "completed")

admin.site.register(Note, NoteAdmin)
admin.site.register(Author, AuthorAdmin)