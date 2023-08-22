
from rest_framework import serializers
from users.models import User,TgUser





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"




class TgUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUser
        fields = "__all__"
