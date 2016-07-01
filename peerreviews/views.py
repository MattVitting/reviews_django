from django.shortcuts import render
from rest_framework import viewsets
from models import Reviewer, Reviewslist
from serializers import ReviewerSerializer, ReviewslistSerializer
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


class ReviewslistViewSet(viewsets.ModelViewSet):
    """
      API endpoint that returns all submissions
      """

    queryset = Reviewslist.objects.all()
    serializer_class = ReviewslistSerializer




