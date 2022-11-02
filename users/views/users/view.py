from rest_framework.generics import ListAPIView, RetrieveAPIView

from users.models import User
from users.serializers import UserSerializer


class UserListView(ListAPIView):
    queryset = User.objects.order_by('username').prefetch_related('location').all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.prefetch_related('location').all()
    serializer_class = UserSerializer
