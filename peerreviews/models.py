from django.db import models
from django.utils import timezone


class Reviewer(models.Model):

    name = models.CharField(max_length=200)
    affiliation = models.TextField(null=True)
    email = models.EmailField(default=None)
    bio = models.TextField(null=True)
    research = models.TextField(null=True)
    website = models.URLField(null=True)
    osfreviews = models.IntegerField(default=0)
    avatar = models.ImageField(blank=True, null=True, upload_to='avatars')

class Author(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField(default=None)


class Reviewslist(models.Model):

    title = models.TextField(null=True)
    conference = models.TextField(null=True)
    reviewdeadline = models.DateField(default=None)
    reviewer = models.ForeignKey(Reviewer)
    author = models.ManyToManyField(Author)
    status = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)
    attachment = models.FileField(blank=True, null=True, upload_to='files')

class Feedback(models.Model):

    reviewer = models.OneToOneField(Reviewer)
    submission = models.OneToOneField(Reviewslist)
    ratingPremise = models.IntegerField(default=0)
    ratingResearch = models.IntegerField(default=0)
    ratingStyle = models.IntegerField(default=0)
    comments = models.TextField(null=True)

