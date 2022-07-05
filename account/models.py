from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""
primary_key=True will make the field PRIMARY KEY for that table (model).
If you don’t specify primary_key=True for any field in your model,
Django will automatically add an AutoField to hold the primary key,
so you don’t need to set primary_key=True on any of your fields unless you want to override the default primary-key behavior
"""
"""
According to documentation, An AutoField is an IntegerField that automatically increments according to available IDs.
One usually won’t need to use this directly because a primary key field will automatically be added to your model if you don’t specify otherwise.
"""
# auto-generated
# auto incrementing
# integer
# not null




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    fathers_name = models.CharField(max_length=25)
    melicode = models.CharField(max_length=10)
    image = models.ImageField(upload_to="profiles/images", blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "حساب کاربری"
        verbose_name_plural = "حساب های کاربری"


