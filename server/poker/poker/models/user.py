from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        app_label = 'poker'

    username = models.CharField(max_length=100)

    def __unicode__(self):
        return self.username
