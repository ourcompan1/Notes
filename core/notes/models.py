from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    password = models.CharField(max_length=255)

    def create_user(self, username, first_name, last_name, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.set_password(password)
        self.save()


class Notes(models.Model):
    note = models.TextField()
    login = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

    def create_note(self, text, user_id):
        self.note = text
        self.login = user_id
        self.save()