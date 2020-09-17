from django.db import models


class Portfolio(models.Model):
	title = models.CharField(max_length=20)
	img = models.ImageField(null=True, blank=True)
	describe = models.CharField(max_length=30)


def __str__(self):
    return self.title


class Meta:
    verbose_name='Портфолио'
    verbose_name_plural = 'Портфолио'