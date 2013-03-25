from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)

    def __unicode__(self):
        return self.username

class UserToken(models.Model):
    userIds = models.OneToOneField(User);
    authToken = models.CharField(max_length=32);

class Table(models.Model):
    name = models.CharField(max_length=32);

