from urllib import request
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


class ForumHome(DataMixin, ListView):
    paginate_by = 3 
    model = Forum
    template_name = 'forum/index.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Main Page'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Main Page'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Forum.objects.filter(is_published=True)


def about(request):
    return render(request, 'forum/about.html', {'menu': menu, 'title': 'About'})

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'forum/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Add Page'
        return context

def contact(request):
    return HttpResponse("Feedback")


def pageNotFound(request, exception):
    return HttpResponse("Page not found")

class ShowPost(DataMixin, DetailView):
    model = Forum
    template_name = 'forum/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'post'
        return context
    
    

class ForumCategory(DataMixin, ListView):
    model = Forum
    template_name = 'forum/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Forum.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Category: ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'forum/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Register'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    

        

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'forum/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Login'
        return context
    
    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')


class ShowProfilePageView(DataMixin, DetailView):
    model = Profile
    template_name = 'forum/user_profile.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class CreateProfilePageView(CreateView):
    model = Profile

    template_name = 'forum/create_profile.html'
    fields = ['profile_pic', 'bio', 'facebook', 'twitter', 'instagram']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('home')


class NewsUpdateView(UpdateView):
    model = Forum
    template_name = 'forum/update_post.html'
    fields = ['title', 'content', 'cat']
    success_url = reverse_lazy('home')


class NewsDeleteView(DeleteView):
    model = Forum
    template_name = 'forum/delete_post.html'
    success_url = reverse_lazy('home')

def news_home(request):
    posts = Forum.objects.all()
    return render(request, 'forum/base.html', {'posts': posts})