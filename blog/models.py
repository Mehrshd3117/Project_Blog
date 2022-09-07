from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.html import format_html
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ساخت")

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
    title = models.CharField(max_length=70, verbose_name="عنوان")
    body = models.TextField(verbose_name="بدنه")
    image = models.ImageField(upload_to="images/articles", blank=True, null=True, verbose_name="عکس")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True, verbose_name="وضعیت")
    published = models.BooleanField(default=True, verbose_name="منتشر شده")
    slug = models.SlugField(blank=True, unique=True, verbose_name="ادرس اینترنتی")
    pub_date = models.DateTimeField(default=timezone.now(),  verbose_name="زمان انتشار")
    objects = models.Manager()
    custom_manager = ArticleManager()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.slug})

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="50px" height="50px">')
        return format_html('<h3 style="color: red">تصویر ندارد</h3>')
    show_image.short_description = " تصویر"

    def __str__(self):
        return f"{self.title} - {self.body[:30]}"

    class Meta:
        ordering = ('-created',)
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name="مقاله")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name="کاربر")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies', verbose_name="والد")
    body = models.TextField(verbose_name="بدنه")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ساخت")

    def __str__(self):
        return self.body[:50]

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"


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


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes", verbose_name="کاربر")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="likes", verbose_name="مقاله")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.article.title}"

    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = "لایک ها "
        ordering = ("-created_at",)
