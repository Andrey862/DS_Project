from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
import socket


def home(request):
    context = {
        'posts': Post.objects.all(),
        'hostname': socket.gethostname()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    extra_context = {
        'hostname': socket.gethostname()
    }


class PostDetailView(DetailView):
    model = Post
    extra_context = {
        'hostname': socket.gethostname()
    }


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    extra_context = {
        'hostname': socket.gethostname()
    }


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    extra_context = {
        'hostname': socket.gethostname()
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    extra_context = {
        'hostname': socket.gethostname()
    }

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
