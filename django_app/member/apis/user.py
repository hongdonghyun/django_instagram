from rest_framework import generics
from rest_framework import permissions

from member.serializers import UserCreationSerializer, UserSerializer
from utils.permissions import ObjectIsRequestUser
from ..models import User

__all__ = (
    'UserRetrieveUpdateDestroyView',
    'UserListCreateView',
)


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        ObjectIsRequestUser,
    )


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return UserSerializer
        elif self.request.method == "POST":
            return UserCreationSerializer
