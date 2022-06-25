from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .models import Post
# Create your views here.

class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post

    fields = [
        "title",
        "slug",
        "author",
        "body",
        "publish",
        "created",
        "updated",
        "status"
    ]

    success_url  = 'list.html'



class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post

    fields = [
        "title",
        "slug",
        "author",
        "body",
        "publish",
        "created",
        "updated",
        "status"
    ]

    success_url  = '/'


class PostDeleteView(DeleteView):
    model = Post

    fields = [
        "title",
        "slug",
        "author",
        "body",
        "publish",
        "created",
        "updated",
        "status"
    ]

    success_url  = '/'
