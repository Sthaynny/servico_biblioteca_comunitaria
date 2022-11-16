from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups' , 'is_superuser','is_staff' , 'password']

    def create(self, validated_data): 
        user = User.objects.create(
        username=validated_data['username'], 
        email=validated_data['email'],  
        is_staff=True,
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
