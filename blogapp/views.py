from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from .forms import BlogPostForm

class BlogView(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'Posts/blogView.html'

class BlogCreateWithFields(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'Posts/blogcreate.html'
    success_url = reverse_lazy('blog_list')

class BlogUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    pk_url_kwarg = 'pk'
    template_name = 'Posts/blogupdate.html'
    success_url = reverse_lazy('blog_list')   # ✅ correction ici

class BlogDeleteView(DeleteView):
    model = BlogPost
    pk_url_kwarg = 'pk'
    template_name = 'Posts/blogdelete.html'
    success_url = reverse_lazy('blog_list')
