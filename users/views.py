from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from users.api.serializers import UserRankingSerializer, UserSerializer
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
        


        
class UserView(APIView):

    def get(self, request):
        if request.user.is_authenticated:


            user = User.objects.get(id=request.user.id)
            serializer = UserSerializer(user).data

            serializer.pop('password')

            return Response(serializer, status=status.HTTP_201_CREATED)

        return Response({'error': 'usuário inválido'}, status=status.HTTP_401_UNAUTHORIZED)


    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer = serializer.data
                user: User = User.objects.create(**serializer)
                user.set_password(serializer['password'])
                user.save()
                return Response(serializer, status=status.HTTP_201_CREATED)
            except:
                return Response({'error': 'dados inválidos'}, status=status.HTTP_400_BAD_REQUEST)    
        else:
            return Response({'error': 'dados inválidos'}, status=status.HTTP_400_BAD_REQUEST)



class UserScoreView(APIView):
    def get(self, request):
        ranking  = User.objects.all().order_by('-score')[:5]
        serializer = UserRankingSerializer(ranking, many=True).data
        return Response(serializer, status=status.HTTP_202_ACCEPTED)


    def post(self, request):
        if request.user:
            userId = request.user.id
            user = User.objects.get(id=userId)
            user.score = user.score + 1
            user.save()
        return Response({'success': 'ok'}, status=status.HTTP_200_OK)

