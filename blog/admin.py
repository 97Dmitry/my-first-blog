from django.contrib import admin
from .models import Post, Rubric, Comments, Rating, ValueRatingPost

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'rubric', 'text', 'author', 'published_date')
	list_display_links = ('title', 'text')
	search_fields = ('author', 'title', 'text')


class CommentsAdmin(admin.ModelAdmin):
	list_display = ('post', 'name', 'comment', 'created')
	list_display_links = ('post', 'name')
	search_fields = ('email',)


class ValueRatingPostAdmin(admin.ModelAdmin):
	list_display = ('user', 'post', 'rating')
	list_display_links = ('post',)


admin.site.register(Post, PostAdmin)
admin.site.register(Rubric)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(ValueRatingPost, ValueRatingPostAdmin)
admin.site.register(Rating)