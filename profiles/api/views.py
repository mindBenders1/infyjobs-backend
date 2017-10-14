from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ..models import UserProfile
from .serializers import UserProfileSerializer

class UserProfileListCreateAPIView(ListCreateAPIView):
	queryset = UserProfile.objects.all()
	permission_classes = (IsAuthenticated,)
	serializer_class = UserProfileSerializer
	lookup_field = 'pk'

class UserProfileRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	queryset = UserProfile.objects.all()
	permission_classes = (IsAuthenticated,)
	serializer_class = UserProfileSerializer
	lookup_field = 'pk'