from django.urls import path
from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter
from users import views

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
urlpatterns = [
    path('payments/', views.PaymentListAPIView.as_view(), name='payment_list'),
] + router.urls
