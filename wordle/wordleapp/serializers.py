import rest_framework.fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        depth = 1
