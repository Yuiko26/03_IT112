from rest_framework import serializers
from .models import BookContributor
from .models import Contributor


class PublisherSerializer(serializers.Serializer):
    name = serializers.CharField()
    website = serializers.URLField()
    email = serializers.EmailField()


class BookSerializer(serializers.Serializer):
    title = serializers.CharField()
    publication_date = serializers.DateField()
    isbn = serializers.CharField()
    publisher = PublisherSerializer()


class ContributionSerializer(serializers.ModelSerializer):
    book = BookSerializer()


    class Meta:
        model = BookContributor
        fields = ['book', 'role']


class ContributorSerializer(serializers.ModelSerializer):
    bookcontributor_set = ContributionSerializer(read_only=True, many=True)
    number_contributions = serializers.ReadOnlyField()


    class Meta:
        model = Contributor
        fields = ['first_names', 'last_names', 'email',
                'bookcontributor_set', 'number_contributions']
