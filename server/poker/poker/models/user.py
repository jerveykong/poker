from poker.base.common.Common import *
from django.db import models
from django.core import serializers

class UserManager:
    def addUser(self, userName):
        user = User()
        user.username = userName
        user.validate()
        user.save()
    def getUser(self, userId):
        user = User.objects.get(pk = userId)
        return user

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    manager = UserManager()

    class Meta:
        app_label = 'poker'

    def __unicode__(self):
        return self.username

    def validate(self):
        if( len(self.username) <= 0 ):
            raise ModelAttributeException("Username must not be empty")
