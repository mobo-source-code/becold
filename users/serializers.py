from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from users.models import CustomUser
from rest_auth.models import TokenModel

class NameRegistrationSerializer(RegisterSerializer):
	username = None
	full_name = serializers.CharField(required=False)
	mobile = serializers.CharField(required=False)
	ville = serializers.CharField(required=False)
	pays = serializers.CharField(required=False)


	
	def custom_signup(self, request, user):
		user.full_name = self.validated_data.get('full_name', '')
		user.mobile = self.validated_data.get('mobile', '')
		user.ville = self.validated_data.get('ville', '')
		user.pays = self.validated_data.get('pays', '')
		user.save(update_fields=['full_name', 'mobile', 
									'ville', 'pays'])


class LoginSerializer(RestAuthLoginSerializer):
	username = None



class UserSerializer(serializers.ModelSerializer):
	username = None
	class Meta:
		model = CustomUser
		fields = ('id', 'email', 'full_name', 'mobile', 
					'ville', 'pays',)
	
	def create(self, validated_data):
		user = CustomUser.objects.create_user(**validated_data)
		Token.objects.create(user=user)
		return user

class TokenSerializer(serializers.ModelSerializer):
	user = UserSerializer(many=False, read_only=True)
	class Meta:
		model = TokenModel
		fields = ('key', 'user')