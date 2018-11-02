from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=70)
    slug  = models.CharField(max_length=25)
    description = models.TextField(null=True, blank=True)
    keywords = models.CharField(max_length=150, null=True, blank=True)
    price = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    active = models.BooleanField()
    category = models.ManyToManyField('Category')
    tags = models.ManyToManyField('tags.Tag')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title
