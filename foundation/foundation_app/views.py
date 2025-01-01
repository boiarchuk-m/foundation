from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, RequestSerializer, UpdateRequestStatusSerializer
from .models import CustomUser, Request
from rest_framework import status
from rest_framework import permissions, viewsets
from .permissions import IsOwner, IsManager


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = CustomUser.objects.filter(username=username).first()
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data,
            })
        return Response({'error': 'Invalid credentials'}, status=400)


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully!'}, status=201)
        return Response(serializer.errors, status=400)


class UserRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_requests = Request.objects.filter(created_by=request.user)
        serializer = RequestSerializer(user_requests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        user_request = Request.objects.get(id=pk, created_by=request.user)
        serializer = RequestSerializer(user_request, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user_request = Request.objects.get(id=pk, created_by=request.user)
        user_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ManagerRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not request.user.role == 'manager':
            return Response(status=status.HTTP_403_FORBIDDEN)
        requests = Request.objects.all()
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)

    def patch(self, request, pk):
        if not request.user.role == 'manager':
            return Response(status=status.HTTP_403_FORBIDDEN)
        req = Request.objects.get(id=pk)
        req.status = request.data.get('status', req.status)
        req.manager_comment = request.data.get('manager_comment', req.manager_comment)
        req.save()
        serializer = RequestSerializer(req)
        return Response(serializer.data)