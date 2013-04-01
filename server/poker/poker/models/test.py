from django.db import models

class UserToken(models.Model):
    userIds = models.OneToOneField(User);
    authToken = models.CharField(max_length=32);

class Table(models.Model):
    name = models.CharField(max_length=32);

