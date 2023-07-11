from django.shortcuts import render,get_object_or_404
from django.views.generic import *
from .models import *
from django.urls import reverse_lazy
# Create your views here.
class home(View):
    def get(self,request):
        return render(request,'home.html')
    
class list(View):
    def get(self,request):
        blog = Blog.objects.all()
        return render(request,'list.html',{'blog':blog})

class details(View):
    def get(self,request,id):
        blog = get_object_or_404(Blog,id=id)
        return render(request,'details.html',{'blog':blog})

class CreateBlog(CreateView):
    model = Blog
    template_name = 'blog_new.html'
    fields = ('title','subtitle','body','image',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    model = Blog
    fields = ('title','subtitle','body','image',)
    template_name = 'article_edit.html'

class ArticleDeleteView(DeleteView):
    model = Blog
    template_name = 'article_delete.html'
    success_url = reverse_lazy('list')