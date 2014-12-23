from django.db import models
from django.contrib.auth.models import User

from geo.models import Geo


class Note(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()
    post_location = models.ForeignKey(Geo, null=True)

    def __str__(self):
        return self.title
