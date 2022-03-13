from django.db import models
from django.urls import reverse


class philosophers(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя философа')
    surname = models.CharField(max_length=100, verbose_name='Фамилия философа')
    philosophy_name = models.CharField(max_length=100, verbose_name='Философия')
    philosophy = models.TextField(verbose_name='Суть философий')
    birth_time = models.DateField(verbose_name='День рождения')
    death_time = models.DateField(verbose_name='День смерти')
    idea = models.ForeignKey( 'philosophy_ideas', on_delete=models.PROTECT,null = True, verbose_name= 'Течения философий')

    def __str__(self):
        return self.philosophy_name

    class Meta:
        verbose_name = 'Философия'
        verbose_name_plural = 'Философий'


class philosophy_ideas(models.Model):
    philosophy_idea_name = models.CharField(max_length=100,verbose_name='Течения философий')

    class Meta:
        verbose_name = 'Идея'
        verbose_name_plural = 'Идеи'

    def __str__(self):
        return self.philosophy_idea_name

    def get_absolute_url(self):
        return reverse('philosophy_idea_name', kwargs={'idea_id': self.pk})
