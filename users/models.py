from django.contrib.auth.models import User
from django.db import models


class Confirm_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)

    def __str__(self):
        return self.code
