from django.db import models
from django.utils import timezone


class Reviewer(models.Model):

    name = models.CharField(max_length=200)
    affiliation = models.TextField()
    email = models.EmailField
    bio = models.TextField
    research = models.TextField
    website = models.URLField
    member_date = models.DateTimeField(
            default=timezone.now)
    number_reviews = models.IntegerField

    #def countReviews(self):
    # add here code to count number of reviews
    #self.number_reviews = xxx
    #self.save()


