from django.db import models


# Create your models here.
class Phone(models.Model):
    name = models.CharField(max_length=60, verbose_name='Название')
    price = models.FloatField(verbose_name='Стоимость')
    image = models.TextField()
    release_date = models.DateTimeField(verbose_name='Дата создания')
    lte_exists = models.BooleanField(default=True, verbose_name='LTE')
    slug = models.SlugField(max_length=120)
