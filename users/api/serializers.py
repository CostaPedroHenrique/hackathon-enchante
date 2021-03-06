from users.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = (
            'username',
            'name',
            'email',
            'birthDate',
            'password',
            'avatar',
            'score',
        )

class UserRankingSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = (
            'username',
            'name',
            'score',
            'avatar',
        )

