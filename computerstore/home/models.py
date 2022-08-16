from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']



class PC(models.Model):
    title = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='title')
    content = models.TextField()
    price = models.PositiveIntegerField(default=0)
    cpu = models.CharField(max_length=50)
    gpu = models.CharField(max_length=50)
    ram = models.PositiveIntegerField(default=0)
    memory = models.PositiveIntegerField(default=0)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('detailpc', kwargs={'slug': self.slug})


class Accessory(models.Model):
    title = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='title')
    content = models.TextField()
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    price = models.PositiveIntegerField(default=0)
    types = models.ForeignKey('Type', on_delete=models.PROTECT, related_name='type')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('detailacc', kwargs={'slug': self.slug})


class Type(models.Model):
    title = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']