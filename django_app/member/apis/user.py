from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from member.serializers import UserSerializer
from ..models import User

__all__ = (
    'UserDetailView',
)


class UserDetailView(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return User.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
