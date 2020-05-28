from django.contrib import admin

from .models import DayOfTheWeek, Department, Course, Teacher, AcademicDiscipline, Provision, TypeSubject, Subject, Group, Curriculum, WorkingHours, TypeClassroom, Classroom, Frequency, Schedule, HalfLesson, TimeSchedule, TableSchedule, Exam, RestDay

admin.site.register(DayOfTheWeek)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(AcademicDiscipline)
admin.site.register(Provision)
admin.site.register(TypeSubject)
admin.site.register(Subject)
admin.site.register(Group)
admin.site.register(Curriculum)
admin.site.register(WorkingHours)
admin.site.register(TypeClassroom)
admin.site.register(Classroom)
admin.site.register(Frequency)
admin.site.register(Schedule)
admin.site.register(HalfLesson)
admin.site.register(TimeSchedule)
admin.site.register(TableSchedule)
admin.site.register(Exam)
admin.site.register(RestDay)