from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import OuterRef, Subquery,Max
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from utils.errorsFormatter import modify_serialize_errors
from .serializers import (UserSignupSerializers, LoginSerializers, CategorySerializer,
                          SubcategorySerializer, UserScapeSerializer, UserGetScapeSerializer)
from user.models import Category, SubCategory, UserScape


class UserSignupView(APIView):
    """
    This view for signup.This view handles the registration of new users.
    it validates user input data,creates new user, and returns appropriate response
    """

    def post(self, request):
        if request.data.get("username"):
            user_name = User.objects.filter(username=request.data['username']).exists()
            if not user_name:
                post_data = UserSignupSerializers(data=request.data)
                if post_data.is_valid():
                    post_data.save()
                    response_data = {
                        "status": 201,
                        "data": post_data.data,
                        "message": "Created",
                        'error': ''

                    }
                    return Response(response_data, status=status.HTTP_201_CREATED)
                else:
                    response_data = {
                        "status": 500,
                        "message": "",
                        'error': post_data.errors

                    }
                    return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                response_data = {
                    "status": 422,
                    "message": "",
                    'error': request.data['username'] + " already Exist"

                }

                return Response(response_data, status=status.HTTP_409_CONFLICT)
        else:
            response_data = {
                "status": 422,
                "message": "",
                'error': 'Some fileds are manadatory. you have fill that!!'

            }

            return Response(response_data, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class LoginView(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializers(data=data)
        if serializer.is_valid():
            user = User.objects.get(username=request.data['username'])
            token = RefreshToken.for_user(user)
            response_data = {
                "status": 200,
                "message": "Login",
                'error': '',
                'refresh': str(token),
                'access': str(token.access_token)

            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            response_data = {
                "status": 401,
                "message": "Invalid username or password",
                'error': ''

            }
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)


class CategoriesView(APIView):

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        response_data = {
            "status": 200,
            "message": "Data Retrieved",
            'error': '',
            'data': serializer.data

        }
        return Response(response_data, status=status.HTTP_200_OK)


class SubCategoryView(APIView):
    def get(self, request, id):
        if id:
            data = SubCategory.objects.filter(parent=id)
            serializer = SubcategorySerializer(data, many=True)
            response_data = {
                "status": 200,
                "message": "Data",
                'error': '',
                'data': serializer.data

            }
            return Response(response_data, status=status.HTTP_200_OK)

        else:
            response_data = {
                "status": 500,
                "message": "ParentCategory Required",
                'error': 'ParentCategory Required',
                'data': ''

            }
            return Response(response_data, status=status.HTTP_200_OK)


class UserScapeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = UserScapeSerializer(data=data)

        if serializer.is_valid():
            serializer.save(is_active=True, user=request.user)
            response_data = {
                "status": 201,
                "message": "Data created",
                'error': '',
                'data': serializer.data

            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            response_data = {
                "status": 500,
                "message": "Error",
                'error': modify_serialize_errors(serializer.errors),
                'data': ''

            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        user = request.user
        # Subquery to get the latest UserScope date for each sub_category
        latest_dates = UserScape.objects.values('sub_category').annotate(
            latest_date=Max('date')
        ).values('sub_category', 'latest_date')
        latest_user_scopes = UserScape.objects.filter(
            date__in=Subquery(latest_dates.values('latest_date'))
        ).select_related('sub_category').order_by('-date')
        serializer = UserGetScapeSerializer(latest_user_scopes, many=True)
        response_data = {
            "status": 200,
            "message": "Data retrieved",
            'error': '',
            'data': serializer.data

        }
        return Response(response_data, status=status.HTTP_200_OK)

