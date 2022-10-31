from django.contrib.auth.models import User
from rest_framework import serializers




class PostSerializer(serializers.ModelSerializer):
    tracks = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
     )

    class Meta:
        model = User
        fields = ['id', 'username']