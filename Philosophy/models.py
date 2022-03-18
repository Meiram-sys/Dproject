from django.db import models
from django.urls import reverse


class philosophers(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя философа')
    surname = models.CharField(max_length=100, verbose_name='Фамилия философа')
    philosophy_name = models.CharField(max_length=100, verbose_name='Философия')
    philosophy = models.TextField(verbose_name='Суть философий')
    birth_time = models.DateField(verbose_name='День рождения')
    death_time = models.DateField(verbose_name='День смерти')

    def __str__(self):
        return self.philosophy_name

    class Meta:
        verbose_name = 'Философия'
        verbose_name_plural = 'Философий'


class Individuals(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя философа')
    surname = models.CharField(max_length=100, verbose_name='Фамилия философа')
    biography = models.TextField(verbose_name='Биография')
    photo = models.ImageField(verbose_name='Фото',null = True)
    birth_time = models.DateField(verbose_name='День рождения')
    death_time = models.DateField(verbose_name='День смерти')
    category= models.ForeignKey('category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.name + self.surname

    class Meta:
        verbose_name = 'Личность'
        verbose_name_plural = 'Личности'


class category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'

