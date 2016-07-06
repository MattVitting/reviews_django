from rest_framework import serializers
from models import Reviewer, Reviewslist, Feedback



class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer

        fields = ('name', 'affiliation', 'email', 'bio', 'research', 'website', 'osfreviews', 'avatar')



class ReviewslistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewslist
        fields = ('title', 'conference', 'reviewdeadline', 'reviewer',  'author', 'status', 'link', 'attachment')


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('reviewer', 'submission', 'ratingPremise', 'ratingResearch', 'ratingStyle', 'comments')
