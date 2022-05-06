from django.contrib import admin
from .models import *

class ForumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_links = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_links = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    search_links = ('name',)
    



admin.site.register(Forum, ForumAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile, ProfileAdmin)




