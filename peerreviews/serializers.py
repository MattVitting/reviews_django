from rest_framework import serializers
from models import Reviewer, Feedback


class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = ('name', 'affiliation', 'email', 'bio', 'research', 'website', 'member_date', 'number_reviews')

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('reviewer', 'submission', 'ratingPremise', 'ratingResearch', 'ratingStyle', 'comments')
