from users.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    print(locals())
    class Meta:
        model=User
        fields = (
            'username',
            'name',
            'email',
            'birthDate',
            'password'
        )