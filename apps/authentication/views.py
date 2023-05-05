from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import CustomTokenObtainPairSerializer, AccessTokenSchema
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing customuser instances.
    """

    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework.exceptions import AuthenticationFailed


class InvalidUser(AuthenticationFailed):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_detail = "Credentials is invalid or expired"
    default_code = "user_credentials_not_valid"


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Authentication endpoint to get access tokens
    """

    @swagger_auto_schema(responses={200: AccessTokenSchema()})
    def post(self, request, *args, **kwargs):
        payload = request.data
        serializer = CustomTokenObtainPairSerializer(data=payload)
        # serializer.is_valid(raise_exception=True)
        try:
            serializer.is_valid(raise_exception=True)
        except AuthenticationFailed as e:
            print("AuthenticationFailed")
            raise InvalidUser(e.args[0])
        except TokenError as e:
            print("TokenError")
            raise InvalidToken(e.args[0])
        response_payload = serializer.validated_data
        print(response_payload)
        return Response(response_payload, status=status.HTTP_200_OK)


class CustomTokenRefreshView(TokenRefreshView):
    """
    Authentication endpoint to get refresh tokens
    """

    @swagger_auto_schema(responses={200: AccessTokenSchema()})
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_payload = serializer.validated_data
        print(response_payload)
        return Response(response_payload, status=status.HTTP_200_OK)
