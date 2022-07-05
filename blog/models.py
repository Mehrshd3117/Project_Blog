import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

class ArticleManager(models.Manager):
    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().filter(status=True)



class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles", verbose_name="نویسنده ی مقاله")
    category = models.ManyToManyField(Category, related_name="artilces", verbose_name="دسته بندی")
    title = models.CharField(max_length=70)
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    floatfield = models.FloatField(default=1)
    myfile = models.FileField(upload_to='test', null=True)
    status = models.BooleanField(default=True)
    published = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, unique=True)
    pud_date = models.DateTimeField(default=timezone.now())
    objects = models.Manager()
    custom_manager = ArticleManager()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title} - {self.body[:30]}"

    class Meta:
        ordering = ('-created',)
        verbose_name = 'مقاله'
        verbose_name_plural = "مقالات"

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True, related_name='replies')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.body[:50]

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'


class Message(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    age = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    date = models.DateTimeField(default=timezone.now())


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"


