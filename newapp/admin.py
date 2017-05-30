from django.contrib import admin

# Register your models here.
from newapp.models import *



class CommentInLine(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    fields = ['title','text','date','category','image']
    search_fields = 'title text'.split()
    list_filter = 'title date'.split()
    list_per_page = 1
    list_display = "title text date".split()
    readonly_fields = 'date'.split()
    inlines = [CommentInLine]

class PostInLine(admin.TabularInline):
    model = Post
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    fields = "name color image_tag".split()
    inlines = [PostInLine]
def image_tag(self):
    return u'<img src="%s" />' % obj.image.url
image_tag.short_description = 'Image'
image_tag.allow_tags = True


admin.site.register(Post,PostAdmin)
admin.site.register(Category, CategoryAdmin)
