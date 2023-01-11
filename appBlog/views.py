from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, DetailView, UpdateView
from appBlog.models import Post, Avatar
from django.urls import reverse_lazy
from appBlog.forms import UsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    posts = Post.objects.order_by("-publicado_el").all()
    return render(request, "appBlog/index.html",{"posts" : posts})

def aboutme(request):
    return render(request, "appBlog/about_me.html", {})

class PostList(ListView):
    model = Post

class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("appBlog-listar")
    fields = "__all__"
    
class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("appBlog-listar")
    
class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("appBlog-listar")
    fields = "__all__"
    
class PostDetalle(DetailView):
    model = Post
    
class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("appBlog-listar")
    
class UserLogin(LoginView):
    next_page = reverse_lazy("appBlog-listar")
    
class UserLogOut(LogoutView):
    next_page = reverse_lazy("appBlog-listar")
    
class AvatarActualizar(UpdateView):
    model = Avatar 
    fields=["imagen"]
    success_url = reverse_lazy("appBlog-listar")
    
class UserActualizar(UpdateView):
    model = User
    fields = ["first_name", "last_name", "email"]
    success_url = reverse_lazy("appBlog-listar")