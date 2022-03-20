from cgitb import reset
from django.shortcuts import render
from rest_framework.views import APIView
from googletrans import Translator
from rest_framework.response import Response
from rest_framework import status



class TranslateView(APIView):
    def get(self, request):
        message = request.GET.get('message', 'bem vindo!')
        translator = Translator()
        textTranslated = translator.translate(message, dest='fr').text

        return Response({'result': textTranslated}, status=status.HTTP_200_OK)