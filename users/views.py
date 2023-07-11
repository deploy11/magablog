from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import CustomUser
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class Profle(View):
     def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        return render(request, 'profile.html', {'customuser':user})