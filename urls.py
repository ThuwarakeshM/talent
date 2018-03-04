from django.urls import path, include
from rest_framework import routers

from core import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('publishers', views.PublisherViewSet)
router.register('applicant', views.ApplicantViewSet)
router.register('telephone', views.TelephoneViewSet)
router.register('web', views.WebViewSet)
router.register('advertisement', views.AdvertisementViewSet)
router.register('application', views.ApplicationViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
