from django.db import models
from django.contrib.auth.models import Group
from django.db import models


# Create your models here.
class Trend(models.Model):

    group = models.OneToOneField(Group)
    # The additional attributes we wish to include.

    def __unicode__(self):
        return self.group.id

