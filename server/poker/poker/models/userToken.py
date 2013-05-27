from django.db import 

class UserToken(models.Model):
    class Meta:
        app_label = 'poker'

    userId = models.CharField(max_length=32)

    def __unicode__(self):
        return self.userId
