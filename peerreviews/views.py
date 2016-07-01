from django.shortcuts import render
from rest_framework import viewsets
from models import Reviewer
from serializers import ReviewerSerializer, AuthenticationSerializer
from django.http import Http404

import requests
from requests_oauth2 import OAuth2
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework import status


USER_STORAGE = {}
# Create your views here.
def post_list(request):
    return render(request, 'peerreviews/test.html', {})

class OsfAuthorizationUrl(APIView):
	def get(self, request, format=None):
		client_id  = '87ccc107d57b44b988abe7fe269bf6ba'
		client_secret = 'vqgPeZslbbGt6kRrZX5FNeB6SincSnB1eevfHjb5'
		oauth2_handler = OAuth2(client_id, client_secret, "https://staging-accounts.osf.io/", "http://localhost:8000/login", authorization_url='oauth2/authorize')
		authorization_url = oauth2_handler.authorize_url('osf.full_read osf.full_write', response_type='code')
		return Response(authorization_url)


class OsfAuthorizationCode(APIView):
	def get(self, request, format=None):
		uid = request.user.id
		CLIENT_ID  = '87ccc107d57b44b988abe7fe269bf6ba'
		CLIENT_SECRET = 'vqgPeZslbbGt6kRrZX5FNeB6SincSnB1eevfHjb5'
		REDIRECT_URI = "http://localhost:8000/login"
		code = request.GET.get('code'); print code, uid
		post_data = { "grant_type": "authorization_code", "code": code, "redirect_uri": REDIRECT_URI, "client_id": CLIENT_ID, "client_secret": CLIENT_SECRET}
		response = requests.post("https://staging-accounts.osf.io/oauth2/token", data=post_data)
		USER_STORAGE[uid] = response
		return Response(USER_STORAGE[uid])

class AuthenticateUser(APIView):
    resource_name = 'User'
    serializer_class = AuthenticationSerializer

    def post(self, request, format=None):
        serializer = AuthenticationSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # the password verified for the user
                login(request, user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # the authentication system was unable to verify the username and password
                return Response("The username and password were not found", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("Incorrect format for POST", status=status.HTTP_404_NOT_FOUND)


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
