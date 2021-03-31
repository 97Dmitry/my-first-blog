from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets

class ProfilesSerializer(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    # def list(self, request):
    #     queryset = Profile.objects.all()
    #     serializer = ProfileSerializer(queryset, many=True)
    #     return Response(serializer.data)

class UserList(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()