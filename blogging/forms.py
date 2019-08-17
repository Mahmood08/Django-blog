from django.forms import ModelForm
<<<<<<< HEAD
from blogging.models import Post
 
class Create_PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text','author']
=======
from blogging.models import CreatePost
 
class CreatePostForm(ModelForm):
    class Meta:
        model = CreatePost
        fields = ['title', 'text', 'author']
>>>>>>> 7f8b50a7ba195d5b6d9dd1cb0990038cf971d629
