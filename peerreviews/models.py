from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group

import datetime


class Reviewer(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=200)
    affiliation = models.TextField(null=True)
    email = models.EmailField(default=None)
    bio = models.TextField(null=True)
    research = models.TextField(null=True)
    website = models.URLField(null=True)
    member_date = models.DateTimeField(default=timezone.now)
    number_reviews = models.IntegerField(default=0)


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(default=None)


class Submission(models.Model):

    title = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    venue = models.TextField(null=True)
    status = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    reviewers = models.ForeignKey(Reviewer)
    reviewdeadline = models.DateField(default=None)
    link = models.URLField(null=True)
    attachment = models.FileField(null=True)
    contributor = models.ForeignKey(Group)

    class Meta:
        ordering = ('date_created',)
