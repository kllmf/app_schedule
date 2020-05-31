from django.contrib import admin

from .models import SpecificDate, Department, Course, Teacher, AcademicDiscipline, Provision, Subject, Group, \
    Curriculum, WorkingHours, Classroom, Schedule, HalfLesson, TableSchedule, Exam, RestDay

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(AcademicDiscipline)
admin.site.register(Provision)
admin.site.register(SpecificDate)
admin.site.register(Subject)
admin.site.register(Group)
admin.site.register(Curriculum)
admin.site.register(WorkingHours)
admin.site.register(Classroom)
admin.site.register(Schedule)
admin.site.register(HalfLesson)
admin.site.register(TableSchedule)
admin.site.register(Exam)
admin.site.register(RestDay)
