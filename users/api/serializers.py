from rest_framework import serializers
from users.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')

    # Django make validation for us
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

# TODO: Add a persion to review all the users activated and deactivated
class UsersSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['id', 'email'] # pending activate and deactivate