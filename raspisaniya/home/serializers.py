from rest_framework import serializers

from .models import Groups, StudentSchedule, TeacherSchedule



class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'



class StudentScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentSchedule
        fields = '__all__'




class TeacherScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherSchedule
        fields = '__all__'


