
from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])