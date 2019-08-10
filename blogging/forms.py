from django.forms import ModelForm
from blogging.models import CreatePost
 
class CreatePostForm(ModelForm):
    class Meta:
        model = CreatePost
        fields = ['title', 'text', 'author']
