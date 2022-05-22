from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_course import views

router = DefaultRouter()
router.register('api_course', views.CourseViewSet)
router.register('lesson', views.LessonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
