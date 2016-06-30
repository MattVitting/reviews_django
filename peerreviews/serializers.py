from rest_framework import serializers
from models import Reviewer, Submission


class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = ('name', 'affiliation', 'email', 'bio', 'research', 'website', 'member_date', 'number_reviews')


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ('title', 'venue', 'status', 'authors', 'reviewers', 'reviewdeadline', 'link', 'attachment')
