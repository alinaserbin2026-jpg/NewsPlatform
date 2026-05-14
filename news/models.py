from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)
    # slug este o variabila scurta , ea se utilizeaza pentru un url mai frumos , in loc de id in format
    # numere se scrie linkul complet ca un fel de titlu
    slug = models.SlugField(max_length=100, unique=True)

    # Este o metoda speciala din python care indica cum trebuie sa reprezinte un obiect in format text
    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)
    # slug este o variabila scurta , ea se utilizeaza pentru un url mai frumos , in loc de id in format
    # numere se scrie linkul complet ca un fel de titlu
    slug = models.SlugField(max_length=200)
    body = RichTextField() #Editor avansat ckeditor
    sumary = models.TextField(max_length=500 , blank=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE, related_name='News')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    image = models.ImageField(upload_to='news/', blank=True)

    publish_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)

    saved_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # clasa interna (nested class) in care se pot defini optiunii de configirare pentru modelul in care se afla
    class Meta:
        ordering = ['-publish_date']
        verbose_name = 'News'

    # Este o metoda speciala din python care indica cum trebuie sa reprezinte un obiect in format text
    def __str__(self):
        return self.title

