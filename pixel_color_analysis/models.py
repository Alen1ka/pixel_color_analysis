from django.db import models


class Images(models.Model):
    img = models.ImageField(upload_to='images/', verbose_name=u"Картинка")
    hex_code = models.CharField(max_length=7, verbose_name=u"Hex-код")
    objects = models.Manager()


class Analysis(models.Model):
    comparison = models.CharField(max_length=100)
    num_pixels_hex = models.IntegerField()
    objects = models.Manager()
