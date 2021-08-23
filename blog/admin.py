from django.contrib import admin
from .models import Author, Post, Tag, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "tags", "date")
    list_display = ("title", "author", "date")

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ("user_name", "post", "date")
    list_filter = ("user_name", "post")

admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
