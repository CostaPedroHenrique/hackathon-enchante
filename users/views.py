from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from rest_framework import status

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserAuth(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                response = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'data': {
                        'username': user.username,
                        'email': user.email
                    }
                }

                return Response(response)
            raise Exception

        except:
            return Response({'error': 'credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        


        
