
from django.db.models import Avg
from rest_framework import serializers
from datetime import date
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('rating'))['rating__avg']
        if rate:
            return round(rate, 1)
        # reviews = obj.reviews.all()
        # if reviews:
        #     return round(sum([review.rating for review in reviews]) / len(reviews))

        return None

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("Resume must have less than 200 characters")

    def validate_release_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Release date must be in the future")
        return value
