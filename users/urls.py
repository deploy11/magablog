from django.urls import path,include
from .views import *


urlpatterns = [
    path('signup/',SignUpView.as_view(),name='signup'),
    path('profile/<str:username>', Profle.as_view(), name='profile'),
]