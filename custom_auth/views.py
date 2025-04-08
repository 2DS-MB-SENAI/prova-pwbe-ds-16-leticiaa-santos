from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def criar_usuario(request):
    username = request.data.get('username')
    senha = request.data.get('senha')
    phone = request.data.get('phone')
    address = request.data.get('address')
    birth_date = request.data.get('birth_date')
    is_verified = request.data.get('verified')

    if not username or not senha or not phone:
        return Response({'Erro': 'Campos obrigatórios incompletos'}, status=status.HTTP_400_BAD_REQUEST)
    
    if CustomUser.objects.filter(username=username).exists():
        return Response({'Erro': f'Username {username} já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    if CustomUser.objects.filter(phone=phone).exists():
        return Response({'Erros': f'telefone {phone} já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    usuario = CustomUser.objects.create_user(
        username=username,
        password=senha,
        phone=phone,
        # address=address,
        # birth_date=birth_date,
        # is_verified=is_verified
    )
    return Response({'Mensagem': f'Usuário {username} criado com sucesso'}, status=status.HTTP_201_CREATED)