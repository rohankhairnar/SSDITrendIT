from django.db import models
from django.contrib.auth.models import User
from django.db import models



# Create your models here.


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username