from django.shortcuts import render
from django.template import loader
from blogging.models import Post
from django import forms
from django.utils import timezone
from blogging.forms import Create_PostForm
from .import forms

from django.http import HttpResponse, HttpResponseRedirect, Http404

def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")



# and this view
"""def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    template = loader.get_template('blogging/list.html')
    context = {'posts': posts}
    body = template.render(context)
    return HttpResponse(body, content_type="text/html")"""

def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'blogging/list.html', context)


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)


            
def create_postview(request):
    
    if request.method == "POST":
        form = forms.Create_PostForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.author= request.user
            model_instance.save()
            return redirect(request,'blogging/list.html',{'post':posts}) 
    else: 
        form = Create_PostForm() 
        return render(request, "blogging/create_post.html", {'form': form})

# Create your views here.
