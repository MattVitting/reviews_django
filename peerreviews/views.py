from django.shortcuts import render
from rest_framework import viewsets
from models import Reviewer, Reviewslist
from serializers import ReviewerSerializer, ReviewslistSerializer
from rest_framework.response import Response
from rest_framework import status
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

    def post(self, request, format=None):
        serializer = ReviewslistSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ReviewslistFilteredViewSet(ListCreateAPIView):
    serializer_class = ReviewslistSerializer

    queryset= Reviewslist.objects.all()

    def get(self, request, rid=None, format=None):
        rl = Reviewslist.objects.filter(reviewer_id=rid)
        ss = ReviewslistSerializer(rl, context={'request': request}, many=True)
        return Response(ss.data)



