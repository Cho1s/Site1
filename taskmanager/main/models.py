from django.db import models

# Create your models here.
class Categorie(models.Model):
    name = models.CharField('Категория', max_length=20)
    slug = models.SlugField(max_length=25, verbose_name='URL')
    description = models.TextField('Описание', max_length=100)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    small_image = models.ImageField(upload_to='static/img/portfolio')
    large_image = models.ImageField(upload_to='static/img/portfolio')
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=25, verbose_name='URL')
    cat = models.ForeignKey('Categorie', on_delete=models.CASCADE, verbose_name='Категория')
    def __str__(self):
        return self.title
