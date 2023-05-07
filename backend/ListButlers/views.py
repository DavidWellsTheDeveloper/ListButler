from rest_framework import viewsets
from .serializers import *
from .models import *

class ListViewSet(viewsets.ModelViewSet):
    serializer_class = ListSerializer
    queryset = List.objects.all()

class ListItemViewSet(viewsets.ModelViewSet):
    serializer_class = ListItemSerializer
    queryset = ListItem.objects.all()

class ListUserViewSet(viewsets.ModelViewSet):
    serializer_class = ListUserSerializer
    queryset = ListUser.objects.all()
