from django.shortcuts import render
from rest_framework import viewsets
from models import Reviewer, Submission
from serializers import ReviewerSerializer, SubmissionSerializer
from rest_framework.response import Response



# Create your views here.
def post_list(request):
    return render(request, 'peerreviews/test.html', {})


class ReviewerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that returns all reviewers.
    """
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer



class ReviewerDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that returns single reviewer by id
    """



    def get(self, request, pk=None, format=None):
        r = Reviewer.objects.filter(id=pk)
        rs = ReviewerSerializer(r, context={'request': request}, many=False)
        return Response(rs.data)


class SubmissionViewSet(viewsets.ModelViewSet):
    """
      API endpoint that returns all submissions
      """

    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer


