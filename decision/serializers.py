from .models import Decision, Point, Discussion
from rest_framework import serializers

class DecisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decision
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Decision.objects.create(**validated_data)

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Point.objects.create(**validated_data)

class DiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussion
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Discussion.objects.create(**validated_data)