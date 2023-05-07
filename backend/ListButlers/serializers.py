from rest_framework import serializers
from .models import *

class ListSerializer(serializers.ModelSerializer):
    item_count = serializers.SerializerMethodField()

    class Meta:
        model = List
        fields = ('id', 'name', 'shared', 'item_count')

    def get_item_count(self, obj):
        return obj.list_items.count()

class ListItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListItem
        # depth = 1
        fields = ('id', 'text', 'list', 'addedBy')

class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListUser
        # depth = 1
        fields = ('id', 'list', 'user', 'owner')