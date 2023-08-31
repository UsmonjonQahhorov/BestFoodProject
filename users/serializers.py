from rest_framework import serializers
from users.models import User, TgUser, Sms
import random
from django.db import models
from rest_framework.exceptions import ValidationError
from twilio.rest import Client
from rest_framework import serializers
from users.models import TgUser, Sms


class TgUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUser
        fields = "__all__"

    def create(self, validated_data):
        instance = super(TgUserSerializer, self).create(validated_data)
        self.send_sms(telegram_user=instance)
        return instance

    def send_sms(self, telegram_user):
        account_sid = 'AC1114bb3082cdbb9e5825451b211fcdc8'
        auth_token = '93eacd87ac6a001cd485c2c823571b75'
        code = random.randint(111111, 999999)
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f'Your code is: {code}. Do not share it with anyone!',
            from_='+19285698468',
            to='+998998787323'
        )
        print("hi barbie")

        print(message.body)

        Sms.objects.create(
            telegram_user=telegram_user,
            sms=code,
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class SmsVerificationSerializer(serializers.Serializer):
    code = serializers.IntegerField(required=True)
    chat_id = serializers.IntegerField(required=True)
