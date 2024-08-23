from datetime import datetime, date as datelib, timezone
from pytz import timezone as tz
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import APIException
from django.db import IntegrityError
from django.contrib.auth import authenticate

from user.models import Category, SubCategory, UserScape


class UserSignupSerializers(serializers.ModelSerializer):
    """
       Serializer for user signup. This serializer is used to handle the
       registration of new users, including validation of input data.
       """

    username = serializers.EmailField()
    password = serializers.CharField(max_length=256, required=True)
    password1 = serializers.CharField(max_length=256, required=True)
    first_name = serializers.CharField(max_length=156, required=True)
    last_name = serializers.CharField(max_length=156, required=True)

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("password1")
        if password != confirm_password:
            response = {"password": "Password must match"}
            raise serializers.ValidationError(response, code=422)
        return attrs

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'password1')

    def save(self):

        data = self.validated_data
        user = User(username=data['username'], email=data['username'], first_name=data['first_name'],
                    last_name=data['last_name'])
        user.set_password(data['password'])
        try:
            user.save()
            return user
        except IntegrityError as exc:
            type(exc)
            raise APIException(detail=exc)


class LoginSerializers(serializers.Serializer):
    """
    This serializer for user login.This serializer used to user
    authentication by validating username and password.
    """
    username = serializers.CharField(max_length=156, required=True)
    password = serializers.CharField(max_length=256, required=True)

    class Meta:
        fields = ('username', 'password')

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        else:
            raise serializers.ValidationError("invalid username or password", code="authorization")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    parent_name = serializers.SerializerMethodField(read_only=True, required=False)

    class Meta:
        model = SubCategory
        fields = ['id', 'title', 'parent', 'is_active', 'created_at',
                  'parent_name']

    def get_parent_name(self, instance):
        if instance.parent:
            return instance.parent.title
        else:
            return ''


class UserScapeSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)
    date = serializers.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%SZ',  # YYYY-MM-DDThh:mm:ssZ
                                                    '%Y-%m-%dT%H:%M',  # YYYY-MM-DDThh:mm:ss
                                                    '%Y-%m-%d',  # YYYY-MM-DD
                                                    '%d-%m-%Y %H:%M:%S',
                                                    '%Y-%m-%d %H:%M:%S',
                                                    ])

    class Meta:
        model = UserScape
        fields = ['id', 'sub_category', 'date', 'short_description', 'is_active', 'created_at', 'updated_at']


class UserGetScapeSerializer(serializers.ModelSerializer):
    main_category = serializers.SerializerMethodField(read_only=True)
    sub_category_name = serializers.SerializerMethodField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    no_of_days = serializers.SerializerMethodField(read_only=True)
    photo = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UserScape
        fields = ['id', 'sub_category', 'user', 'date', 'short_description', 'is_active', 'created_at', 'updated_at',
                  'main_category',
                  'sub_category_name', 'no_of_days', 'photo']

    def get_main_category(self, instance):
        if instance.sub_category:
            return instance.sub_category.parent.title
        else:
            return ''

    def get_sub_category_name(self, instance):
        if instance.sub_category:
            return instance.sub_category.title
        else:
            return ''

    def get_no_of_days(self, instance):
        if instance.date:
            today = datetime.now()
            today = today.replace(tzinfo=tz('UTC'))
            date = instance.date
            diff = today - date
            days, remainder = divmod(diff.total_seconds(), 86400)
            h, s = divmod(remainder, 3600)

            print(f"Hour ==>{h} Seconds ==>{s}")
            m, s = divmod(s, 60)

            return f"{int(days)} days    {int(h)}  hours   {int(m)}   minutes ago"

        else:
            return ''
    def get_photo(self, instance):
        if instance.sub_category:
            return ''
        else:
            return ''