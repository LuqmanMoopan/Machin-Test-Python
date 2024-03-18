
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rideapi.models import Ride
from rideapi.serializers import UserSerializer, RideSerializer, RideStatusUpdateSerializer,RideLocationUpdateSerializer
from rest_framework.decorators import action


class UserRegistrationViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        return Response({"message": "This is the register page."})

class UserLoginViewSet(viewsets.ViewSet):
    def create(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
    def list(self, request):
        return Response({"message": "This is the login page."})
    

class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

    def create_ride(self, serializer):
        serializer.save(rider=self.request.user)  

class RideLocationUpdateViewSet(viewsets.ViewSet):
    @action(detail=True, methods=['patch'])
    def update_location(self, request, pk=None):
        try:
            ride = Ride.objects.get(pk=pk)
        except Ride.DoesNotExist:
            return Response({'error': 'Ride not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = RideLocationUpdateSerializer(data=request.data)
        if serializer.is_valid():
            latitude = serializer.validated_data['latitude']
            longitude = serializer.validated_data['longitude']

            ride.current_latitude = latitude
            ride.current_longitude = longitude
            ride.save()

            return Response({'message': 'Ride location updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RideStatusUpdateViewSet(viewsets.ViewSet):
    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        try:
            ride = Ride.objects.get(pk=pk)
        except Ride.DoesNotExist:
            return Response({'error': 'Ride not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = RideStatusUpdateSerializer(instance=ride, data={'status':request.data.get('status')}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Ride status updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

  