from django.shortcuts import render
from rest_framework import viewsets
from models import Reviewer
from serializers import ReviewerSerializer

# Create your views here.
def post_list(request):
    return render(request, 'peerreviews/test.html', {})


class ReviewerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reviewers to be CRUDed.
    """
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer