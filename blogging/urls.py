from django.urls import path
from blogging.views import stub_view
from blogging.views import list_view, detail_view, create_postview


#app_name = 'blogging'

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('create/', create_postview, name="create"),
    
#    path('', list_view, name="blog_index"),
    
]
