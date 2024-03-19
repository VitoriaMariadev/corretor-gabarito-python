from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Create(models.Model):
    user_name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    # def save(self, *args, **kwargs):
    #     if not self.id:  # Se o objeto ainda não foi salvo no banco de dados
    #         self.password = make_password(self.password)
    #     super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.user_name} {self.password}'