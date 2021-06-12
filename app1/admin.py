from django.contrib import admin
from .models import Teacher,Student


class TeacherAdmin(admin.ModelAdmin):
    #list_display = ('id', 'tname', 'tage', 'tgender') #自選欄位
    list_display = [field.name for field in Teacher._meta.fields] #所有欄位


class StudentAdmin(admin.ModelAdmin):
    #list_display = ('id', 'sname', 'sage', 'sgender', 's_t') #自選欄位
    list_display = [field.name for field in Student._meta.fields] #所有欄位


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)