from django.shortcuts import render
from rest_framework import viewsets
from models import Reviewer, Reviewslist
from serializers import ReviewerSerializer, ReviewslistSerializer
from rest_framework.response import Response
from rest_framework import filters

from rest_framework.generics import ListCreateAPIView


# Create your views here.
def post_list(request):
    return render(request, 'peerreviews/test.html', {})


class ReviewerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that returns all reviewers.
    """
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer



class ReviewslistViewSet(viewsets.ModelViewSet):
    """
      API endpoint that returns all submissions
      """

    queryset = Reviewslist.objects.all()
    serializer_class = ReviewslistSerializer





class ReviewslistFilteredViewSet(ListCreateAPIView):
    serializer_class = ReviewslistSerializer

    queryset= Reviewslist.objects.all()

    def get(self, request, rid=None, format=None):
        rl = Reviewslist.objects.filter(reviewer_id=rid)
        ss = ReviewslistSerializer(rl, context={'request': request}, many=True)
        return Response(ss.data)

