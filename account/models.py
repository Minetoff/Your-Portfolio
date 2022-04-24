from django.db import models


class profil(models.Model):
    name = models.CharField(max_length=150)
    about = models.CharField(max_length=500)
    link = models.URLField(max_length=300)
    photo = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Изображения')

    def __str__(self):
        return self.name


class achieve(models.Model):
    name = models.CharField(max_length=150)
    stepen = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Изображение')

    def __str__(self):
        return self.name