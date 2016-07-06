"""reviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib import admin
from django.conf.urls import include, url
from peerreviews.views import ReviewerViewSet, ReviewslistViewSet, ReviewslistFilteredViewSet
from rest_framework import routers
from django.contrib.staticfiles.urls import static
from django.conf import settings


router = routers.DefaultRouter()
router.register(r'reviewers', ReviewerViewSet)
router.register(r'reviewslists', ReviewslistViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('peerreviews.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api/reviewers/(?P<rid>[0-9]+)/reviews/', ReviewslistFilteredViewSet.as_view(), name='list'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

