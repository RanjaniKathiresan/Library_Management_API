from django.shortcuts import redirect, render
from .serializers import SignUpSerializer, BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('register') 


class RegisterUser(APIView):
    def post(self, request):
        serializer =  SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddBooks(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser] 
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(add_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)