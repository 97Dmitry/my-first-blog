from django.contrib import admin
from .models import Post, Rubric

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'rubric', 'text', 'author', 'published_date')
	list_display_links = ('title', 'text')
	search_fields = ('author', 'title', 'text')


admin.site.register(Post, PostAdmin)
admin.site.register(Rubric)
