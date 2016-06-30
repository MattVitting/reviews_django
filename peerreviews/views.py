from django.shortcuts import render
from rest_framework import viewsets
from models import Reviewer
from serializers import ReviewerSerializer
from django.http import Http404
from rest_framework.response import Response



# Create your views here.
def post_list(request):
    return render(request, 'peerreviews/test.html', {})


class ReviewerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reviewers to be CRUDed.
    """
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer



class ReviewerDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows single reviewer to be CRUDed.
    """



    def get(self, request, pk=None, format=None):
        r = Reviewer.objects.filter(id=pk)
        rs = ReviewerSerializer(r, context={'request': request}, many=False)
        return Response(rs.data)


