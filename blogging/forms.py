from django.forms import ModelForm
from blogging.models import Create_Post
 
class Create_PostForm(ModelForm):
    class Meta:
        model = Create_Post
        fields = ['title', 'text']
