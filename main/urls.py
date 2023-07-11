from django.urls import path
from .views import *


urlpatterns = [
    path('',home.as_view(),name='home'),
    path('blog/',list.as_view(),name='list'),
    path('blog/<int:id>/detail/',details.as_view(),name='detail'),
    path('blog/new/',CreateBlog.as_view(),name='new'),
    path('blog/<int:pk>/edit/', ArticleUpdateView.as_view(), name="article_edit"),
    path('blog/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
]