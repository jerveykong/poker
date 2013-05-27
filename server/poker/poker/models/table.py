from django.db import models

class Table(models.Model):
    class Meta:
        app_label = 'poker'

    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name
