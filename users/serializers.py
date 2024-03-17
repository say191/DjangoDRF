from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from users.models import User, Payment
from materials.models import Course


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'phone', 'city', 'avatar')


class PaymentSerializer(serializers.ModelSerializer):
    paid_course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())

    class Meta:
        model = Payment
        fields = '__all__'
        