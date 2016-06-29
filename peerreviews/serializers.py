from rest_framework import serializers
from models import Reviewer


class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = ('name', 'affiliation', 'email', 'bio', 'research', 'website', 'member_date', 'number_reviews')

