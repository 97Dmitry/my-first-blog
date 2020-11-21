from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'text', 'author', 'published_date')
	list_display_links = ('title', 'text')
	search_fields = ('author', 'title', 'text')

admin.site.register(Post, PostAdmin)
