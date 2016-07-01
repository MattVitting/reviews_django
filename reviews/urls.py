from django.contrib import admin
from django.conf.urls import include, url
from peerreviews import views as peerviews
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'reviewers', peerviews.ReviewerViewSet)
router.register(r'reviewers/(?P<reviewer_id>[0-9]+)/$', peerviews.ReviewerDetailsViewSet.as_view({'get': 'retrieve'}),base_name='reviewer-details')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'', include('peerreviews.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^auth/', peerviews.OsfAuthorizationUrl.as_view(), name='auth'),
    url(r'^login/', peerviews.OsfAuthorizationCode.as_view(), name='login'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^authenticate/', peerviews.AuthenticateUser.as_view(), name='authenticate'),
]
