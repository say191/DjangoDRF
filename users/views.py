from rest_framework.viewsets import generics
from users.serializers import UserSerializer, PaymentSerializer
from users.models import User, Payment
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from users.services import create_stripe_product_and_price, create_stripe_session
from datetime import datetime


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        password = serializer.data['password']
        user = User.objects.get(email=serializer.data['email'])
        user.set_password(password)
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'pay_method')
    orderinf_fields = ('pay_date',)
    permission_classes = [IsAuthenticated]


class PaymentCreateApiView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        payment = serializer.save()
        stripe_price_id = create_stripe_product_and_price(payment)
        payment.payment_link, payment.payment_id, payment.status = create_stripe_session(stripe_price_id)
        payment.pay_date = datetime.now().date()
        payment.save()
