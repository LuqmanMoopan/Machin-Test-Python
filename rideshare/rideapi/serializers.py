from rest_framework import serializers
from django.contrib.auth.models import User
from rideapi.models import Ride

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class RideSerializer(serializers.ModelSerializer):
    rider = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    driver = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username', allow_null=True)

    class Meta:
        model = Ride
        fields = '__all__'

class RideLocationUpdateSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    class Meta:
        model = Ride
        fields = ['latitude','longitude']

class RideStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['status']
