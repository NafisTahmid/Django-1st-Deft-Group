from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField(unique = True, blank = True, null = True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            while Category.objects.filter(slug = self.slug).exists():
                self.slug = f'{slugify(self.title)}-{get_random_string(4)}'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
       

class BlogPost(models.Model):
    STATUS = [
        ('draft', 'Draft'),
        ('published', 'Published')
    ]
    title = models.CharField(max_length = 200)
    slug = models.SlugField(unique = True, blank=True, null = True)
    featured = models.ImageField(upload_to="blogs/", blank=True, null=True)
    content = models.TextField()
    created = models.DateField(auto_now_add = True)
    updated = models.DateField(auto_now = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    status = models.CharField(max_length=10, choices = STATUS, default = 'draft')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            while BlogPost.objects.filter(slug = self.slug).exists():
                self.slug = f'{slugify(self.title)}-{get_random_string(4)}'
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'All Posts'

    def __str__(self):
        return self.title



