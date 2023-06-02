from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Resume


class UserSerializer(serializers.ModelSerializer):
    every_resume = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'every_resume']

class ResumeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Resume
        fields = '__all__'
