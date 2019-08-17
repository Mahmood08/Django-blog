from django.contrib import admin
from blogging.models import Post, Category, CreatePost

class CategoryInline(admin.TabularInline):
    model = Category.posts.through
    

class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline, ]
  

class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts", )

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

<<<<<<< HEAD
#admin.site.register(Post)
=======
admin.site.register(CreatePost)
>>>>>>> 7f8b50a7ba195d5b6d9dd1cb0990038cf971d629
