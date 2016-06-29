

from django.contrib import admin
from .models import Reviewer,Author,Submission

admin.site.register(Reviewer)
admin.site.register(Author)
admin.site.register(Submission)