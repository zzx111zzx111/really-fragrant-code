from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Account(models.Model):
    class Meta:
        db_table = 'account'

    nickname = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=129)


class User(models.Model):
    class Meta:
        db_table = 'user'

    class Sex(models.TextChoices):
        MAN = 'man', _('man')
        WOMAN = 'woman', _('woman')
        SECRET = 'secret', _('secret')

    true_name = models.CharField(max_length=32, blank=True, null=True)

    sex = models.CharField(max_length=6, choices=Sex.choices, default=Sex.SECRET)

    birthday = models.DateTimeField(blank=True, null=True)
    tel = models.CharField(max_length=11, unique=True, blank=True, null=True)
    mail = models.EmailField(max_length=64, unique=True, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    head = models.ImageField(max_length=16, blank=True, null=True)
