from django.forms import ModelForm
from blogging.models import Post
 
class Create_PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text','author']
