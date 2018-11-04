from django.db import models

class Subscribe(models.Model):
    email =  models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    hidden = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Subscribe'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return self.email
