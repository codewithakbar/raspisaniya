from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from mptt.admin import DraggableMPTTAdmin


from .models import Groups, StudentSchedule, TeacherSchedule


@admin.register(Groups)
class BannerAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title')
    mptt_indent_field = "name"
    group_fieldsets = True



@admin.register(StudentSchedule)
class StudentScheduleAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title')
    mptt_indent_field = "name"
    group_fieldsets = True



@admin.register(TeacherSchedule)
class TeacherScheduleAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title')
    mptt_indent_field = "name"
    group_fieldsets = True



