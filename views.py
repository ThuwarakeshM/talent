from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser

from core.permissions import *
from core.serializers import *
from .models import *


# Create your views here.


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TelephoneViewSet(viewsets.ModelViewSet):
    queryset = Telephone.objects.all()
    serializer_class = TelephoneSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WebViewSet(viewsets.ModelViewSet):
    queryset = Web.objects.all()
    serializer_class = WebSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsPublisherOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(
            publisher=Publisher.objects.get(user=self.request.user)
        )


class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsPublisherOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(
            publisher=Publisher.objects.get(user=self.request.user)
        )


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(advertisement=Advertisement.objects.get(pk=self.request.data['advertisement']),
                        applicant=Applicant.objects.get(user=self.request.user),
                        cv=self.request.data['cv'])
