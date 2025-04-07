from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer



User = get_user_model()

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            data = request.data
            first_name = data.get("first_name")
            last_name = data.get("last_name")
            email = data.get("email")
            password = data.get("password")
            confirm_password = data.get("confirm_password")
            is_realtor = data.get("is_realtor")

            if is_realtor == 'True':
                is_realtor = True
            else:
                is_realtor = False


            if password != confirm_password:
                return Response(
                    {"error": "Passwords do not match."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if len(password) < 8:
                return Response(
                    {"error": "Password must be at least 8 characters long."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            
            if User.objects.filter(email=email).exists():
                return Response(
                    {'error': 'Email already exists.'},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            
            if is_realtor:
                user = User.objects.create_realtor(
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password
                )
                return Response(
                    {"message": "Realtor account created successfully."},
                    status=status.HTTP_201_CREATED,
                )
            else:
                user = User.objects.create_user(
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password
                )
                return Response(
                    {"message": "User account created successfully."},
                    status=status.HTTP_201_CREATED,
                )
        
        except:
            return Response(
                {"error": "An error occurred during registration."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        

class RetrieveUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(
                {"error": "An error occurred while retrieving user data."},
                status=status.HTTP_400_BAD_REQUEST,
            )