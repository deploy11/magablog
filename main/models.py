from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=150)
    body = RichTextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        blank=True,null=True
    )
    image = models.ImageField(upload_to='rasmlar/',null=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('list')