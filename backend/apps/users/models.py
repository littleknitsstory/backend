from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm


class AuthorUser(User):
    userpic = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class AuthorForm(ModelForm):
    class Meta:
        model = AuthorUser
        fields = ['userpic', 'title', 'birth_date']

# class CustomerUser(User):
#
#     class Meta:
#         proxy = True  # If no new field is added.
