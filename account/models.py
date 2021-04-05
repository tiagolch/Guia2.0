from django.contrib.auth.models import AbstractUser
from django.db import models
from ministerio.models import Ministerio, Funcao


class User(AbstractUser):
    funcao = models.ManyToManyField(Funcao)






