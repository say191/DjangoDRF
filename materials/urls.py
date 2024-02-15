from django.urls import path
from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter
from materials import views

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet, basename='courses')
urlpatterns = [
    path('lesson/create/', views.LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lessons/', views.LessonListAPIView.as_view(), name='lesson_list'),
    path('lessons/<int:pk>/', views.LessonRetrieveAPIView.as_view(), name='lesson_get'),
    path('lessons/update/<int:pk>/', views.LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lessons/delete/<int:pk>/', views.LessonDestroyAPIView.as_view(), name='lesson_delete')
] + router.urls
