from django.db import models


class philosophers(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя философа')
    surname = models.CharField(max_length=100, verbose_name='Фамилия философа')
    philosophy_name = models.CharField(max_length=100, verbose_name='Философия')
    philosophy = models.TextField(verbose_name='Суть философий')
    birth_time = models.DateField(verbose_name='День рождения')
    death_time = models.DateField(verbose_name='День смерти')

    def __str__(self):
        return self.philosophy_name
