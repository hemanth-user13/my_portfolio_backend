from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *
from .services import *
# Create your views here.
class UserChat(APIView):
    def post(self,request):
        print(request.data)
        user_input=request.data.get("user_input")
        if not user_input:
            return Response({
                "error":"user input is required"
            },status=400)
        
        api_response=generate_api_response(user_input)
        print(api_response)
        chat=UserChatMessage.objects.create(
            user_input=user_input,
            api_response=api_response
        )
        return Response({
            "status":"success",
            "data":{ "user_input": chat.user_input,
            "ai_response": chat.api_response,
            "created_at": chat.created_at},

        },status=201)
