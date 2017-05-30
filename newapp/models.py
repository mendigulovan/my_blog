# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from redactor.fields import RedactorField


def upload_image(instance, filename):
    return 'images/%s'%filename
# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'категории'
        verbose_name = 'категорию'
    image = models.ImageField(upload_to=upload_image, null=True, verbose_name='картинка')
    name = models.CharField(max_length=50, verbose_name='Название')
    color = models.CharField(max_length=50,blank=True, verbose_name="Цвет")

    def __unicode__(self):
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name_plural = 'посты'
        verbose_name = 'пост'
    image = models.ImageField(upload_to=upload_image, null=True, verbose_name='картинка')
    category = models.ForeignKey(Category, null=True,verbose_name='категория')
    title = models.CharField(max_length=100,blank=True,verbose_name='название')
    text = RedactorField(upload_to=upload_image,allow_image_upload=True,verbose_name='текст')
    date = models.DateTimeField(blank=True,null=True,auto_now=True,verbose_name='дата')


    def __unicode__(self):
        return self.title
    def get_text(self):
        return '%s'%(self.text[0:40])

class Comment(models.Model):
    autor = models.CharField(max_length=50)
    text = models.TextField()
    post_comment = models.ForeignKey(Post, null=True)




