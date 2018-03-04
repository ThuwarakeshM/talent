from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Publisher, Application, Applicant, Telephone, Web, Advertisement, Following, Interview


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    web = serializers.HyperlinkedIdentityField(source='web.link',
                                               view_name='web-detail')
    advertisements = serializers.HyperlinkedIdentityField(source='advertisement.title',
                                                          view_name='advertisement-detail')

    class Meta:
        model = Publisher
        fields = (
            'url',
            'id',
            'business_name',
            'industry',
            'street_address',
            'district',
            'user',
            'web',
            'advertisements',
        )


class ApplicantSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Applicant
        fields = ('url', 'id', 'first_name', 'last_name', 'street_address', 'district', 'town', 'user')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    publisher = serializers.HyperlinkedIdentityField(
        view_name='publisher-detail',
        read_only=True,
    )
    applicant = serializers.HyperlinkedIdentityField(
        view_name='applicant-detail',
        read_only=True,
    )

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'publisher', 'applicant')


class TelephoneSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Telephone
        fields = ('url', 'id', 'user', 'number')


class WebSerializer(serializers.HyperlinkedModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.business_name')

    class Meta:
        model = Web
        fields = ('url', 'id', 'publisher', 'link')


class AdvertisementSerializer(serializers.HyperlinkedModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.business_name')

    class Meta:
        model = Advertisement
        fields = (
            'url',
            'publisher',
            'id',
            'opening_date',
            'closing_date',
            'title',
            'description',
            'salary',
            'contract_type',
        )


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    advertisement = serializers.IntegerField(source='advertisement.id')
    applicant = serializers.ReadOnlyField(source='applicant.first_name')

    class Meta:
        model = Application
        fields = ('url', 'id', 'advertisement', 'applicant', 'cv')


class FollowingSerializer(serializers.HyperlinkedModelSerializer):
    applicant = serializers.ReadOnlyField(source='applicant.first_name')
    publisher = serializers.IntegerField(source='publisher.id')

    class Meta:
        model = Following
        fields = ('url', 'id', 'applicant', 'publisher')


class InterviewSerializer(serializers.HyperlinkedModelSerializer):
    application = serializers.IntegerField(source='application.id')

    class Meta:
        model = Interview
        fields = ('url', 'id', 'datetime', 'venue', 'description', 'application')
