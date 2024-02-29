from django.urls import path
from users.apps import UsersConfig
from users import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = UsersConfig.name

urlpatterns = [
    path('create/', views.UserCreateAPIView.as_view(), name='user_create'),
    path('', views.UserListAPIView.as_view(), name='user_list'),
    path('<int:pk>/', views.UserRetrieveAPIView.as_view(), name='user_get'),
    path('update/<int:pk>/', views.UserUpdateAPIView.as_view(), name='user_update'),
    path('delete/<int:pk>/', views.UserDestroyAPIView.as_view(), name='user_delete'),
    path('payments/', views.PaymentListAPIView.as_view(), name='payment_list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
