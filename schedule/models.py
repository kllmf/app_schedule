from django.db import models


# TODO: для всех связей установить delete_on
class DayOfTheWeek(models.Model):  # День недели
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Department(models.Model):  # Кафедра
    name = models.CharField(max_length=100, help_text="Имя кафедры")
    code = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Course(models.Model):  # Направление
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    name = models.CharField(max_length=100, help_text="Имя направления")
    code = models.CharField(max_length=30)
    section = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):  # Преподователь
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    surname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    position = models.CharField(max_length=100)  # TODO: мб создать еще одну модель

    def __str__(self):
        return '%s, %s' % (self.surname, self.first_name)


class AcademicDiscipline(models.Model):  # Дисциплина
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Provision(models.Model):  # Софт(оборудование)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TypeSubject(models.Model):  # Тип предмета(с,л,лаб)
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type


class Subject(models.Model):  # Предмет
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    academic_discipline = models.ForeignKey(AcademicDiscipline, on_delete=models.CASCADE)
    type_subject = models.ForeignKey(TypeSubject, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.academic_discipline.name, self.type_subject.type)


class Group(models.Model):  # Группа
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    the_size_of_the_group = models.IntegerField()

    def __str__(self):
        return self.name


class Curriculum(models.Model):  # Учебныц план
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    number_of_hours = models.IntegerField()


class WorkingHours(models.Model):  # Рабочее время преподавателя
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day_of_the_week = models.ForeignKey(DayOfTheWeek, on_delete=models.CASCADE)

    the_daily_starting_time = models.TimeField()
    number_of_working_hours = models.TimeField()


class TypeClassroom(models.Model):  # Тип аудитории
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Classroom(models.Model):  # Аудитория
    department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)
    provision = models.ManyToManyField(Provision)

    auditorium_number = models.CharField(max_length=50)
    type = models.ForeignKey(TypeClassroom, null=True, on_delete=models.CASCADE)
    capacity = models.IntegerField()

    # TODO: мб добавить корпус

    def __str__(self):
        return self.auditorium_number


class Frequency(models.Model):  # Периоличность(1 нед, 2 нед ...)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class HalfLesson(models.Model):  # Промежуток полупары
    time_start = models.TimeField()
    time_end = models.TimeField()

    def __str__(self):
        return '%s - %s' % (self.time_start, self.time_end)


class TableSchedule(models.Model):  # Общее расписание
    semester = models.IntegerField()
    mod_date = models.DateField()

    def __str__(self):
        return 'Семестр %s (%s)' % (self.semester, self.mod_date)


class Schedule(models.Model):  # Занятие группы без времени
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    day_of_the_week = models.ForeignKey(DayOfTheWeek, on_delete=models.CASCADE)
    frequency = models.ForeignKey(Frequency, on_delete=models.CASCADE)
    half_lesson = models.ForeignKey(HalfLesson, on_delete=models.CASCADE)
    table_schedule = models.ManyToManyField(TableSchedule)
    duration = models.TimeField()


class Exam(models.Model):  # Экзамен
    academic_discipline = models.ForeignKey(AcademicDiscipline, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    exam_date = models.DateField()


class RestDay(models.Model):  # Выходной день
    table_schedule = models.ForeignKey(TableSchedule, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    rest_day = models.DateField()
