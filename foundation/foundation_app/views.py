from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, RequestSerializer, UpdateRequestStatusSerializer
from .models import CustomUser, Request
from rest_framework import permissions, viewsets
from .permissions import IsOwner, IsManager
from rest_framework.decorators import action


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

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        This view returns a list of all the requests for the currently authenticated user.
        """
        return Request.objects.filter(user=self.request.user)


class ManagerRequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticated, IsManager]

    @action(detail=True, methods=['put'])
    def change_status(self, request, pk=None):
        """
        Change the status of a request for managers only.
        """
        request_obj = self.get_object()
        status = request.data.get('status')
        comment = request.data.get('manager_comment', '')

        if status not in ['approved', 'denied', 'need_clarification']:
            return Response({'detail': 'Invalid status'}, status=400)

        request_obj.status = status
        request_obj.manager_comment = comment
        request_obj.save()
        return Response(RequestSerializer(request_obj).data)