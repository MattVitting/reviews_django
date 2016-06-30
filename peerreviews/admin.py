

from django.contrib import admin
from .models import Reviewer,Author,Submission, Feedback

admin.site.register(Reviewer)
admin.site.register(Author)
admin.site.register(Submission)
admin.site.register(Feedback)
