from django.db import models
from django.utils import timezone


class Reviewer(models.Model):

    name = models.CharField(max_length=200)
    affiliation = models.TextField(null=True)
    email = models.EmailField(default=None)
    bio = models.TextField(null=True)
    research = models.TextField(null=True)
    website = models.URLField(null=True)
    member_date = models.DateTimeField(
            default=timezone.now)
    number_reviews = models.IntegerField(default=0)




