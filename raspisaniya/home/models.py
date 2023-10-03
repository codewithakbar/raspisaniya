from django.db import models

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from ckeditor.fields import RichTextField



class Groups(MPTTModel):

    title = models.CharField(max_length=233)

    # bo'lshi shart
    parent = TreeForeignKey('self', on_delete=models.CASCADE, related_name="ona", null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
        

class StudentSchedule(MPTTModel):

    groups = TreeForeignKey(to=Groups, on_delete=models.CASCADE, related_name="tablitsya")
    full_desc = RichTextField()

    parent = TreeForeignKey('self', on_delete=models.CASCADE, related_name="rasisand", null=True, blank=True)


    def __str__(self) -> str:
        return self.groups.title + "ning raspisaniyasi"



class TeacherSchedule(MPTTModel):

    groups = TreeForeignKey(to=Groups, on_delete=models.CASCADE, related_name="tableitsya")
    full_desc = RichTextField()

    parent = TreeForeignKey('self', on_delete=models.CASCADE, related_name="ddd", null=True, blank=True)


    def __str__(self) -> str:
        return "O'qtuvchini" + self.groups.title + "dagi raspisaniyasi"
