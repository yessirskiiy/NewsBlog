from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView

from .models import Post, Comment


class NewsList(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'


class NewsDetail(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'news/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        return context


class NewsCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['text', 'title', 'image']
    success_url = reverse_lazy('news')
    template_name = 'news/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NewsCreate, self).form_valid(form)


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']
    success_url = reverse_lazy('news')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['post_id']
        form.instance.author = self.request.user
        return super().form_valid(form)


class NewsDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('news')
    context_object_name = 'post'


class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('news')
    context_object_name = 'comment'


class NewsEdit(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['text', 'title', 'image']
    success_url = reverse_lazy('news')
    template_name = 'news/post_edit.html'


class UserLogin(LoginView):
    next_page = 'news'
    fields = '__all__'
    template_name = 'news/login.html'


class UserRegistration(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('news')
    template_name = 'news/registration.html'

    def form_valid(self, form):
        user = form.save()
        if form.is_valid():
            login(self.request, user)
        return super(UserRegistration, self).form_valid(form)
