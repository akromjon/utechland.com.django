from django.db import models
from django.utils.text import slugify
# Create your models here.
from django.contrib import admin


class Category(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(editable=False)

    def save(self):

        if not self.id:
            self.slug = slugify(self.title)

        super(Category, self).save()

    def __str__(self) -> str:

        return self.title


class Blog(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(editable=False)
    img = models.ImageField(null=True,upload_to='blog/static/uploads')
    content = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self):

        if not self.id:

            self.slug = slugify(self.title)

        super(Blog, self).save()

    def __str__(self) -> str:
        return f"{self.title} - {self.created_at}"


admin.site.register(Blog)
admin.site.register(Category)
