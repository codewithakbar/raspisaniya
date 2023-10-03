from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'groups', views.GroupsViewSet)
router.register(r'student/(?P<group_id>\d+)', views.StudentScheduleViewSet, basename='schedule')

# router.register(r'student-schedule', views.StudentScheduleViewSet)
router.register(r'teacher-schedule', views.TeacherScheduleViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
