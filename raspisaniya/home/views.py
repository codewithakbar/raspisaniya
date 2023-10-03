from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Groups, StudentSchedule, TeacherSchedule
from .serializers import GroupsSerializer, StudentScheduleSerializer, TeacherScheduleSerializer



class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class StudentScheduleViewSet(viewsets.ModelViewSet):
    # queryset = StudentSchedule.objects.all()
    serializer_class = StudentScheduleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        group_id = self.kwargs['group_id']
        queryset = StudentSchedule.objects.filter(groups__id=group_id)
        return queryset



class TeacherScheduleViewSet(viewsets.ModelViewSet):
    queryset = TeacherSchedule.objects.all()
    serializer_class = TeacherScheduleSerializer
    permission_classes = [IsAuthenticated]
