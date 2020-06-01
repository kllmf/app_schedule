from django.db import models
import datetime

# TODO: для всех связей установить delete_on

day_of_the_week_choice = (('Пн', 'Понедельник'),
                          ('Вт', 'Вторник'),
                          ('Ср', 'Среда'),
                          ('Чт', 'Четверг'),
                          ('Пт', 'Пятница'),
                          ('Сб', 'Суббота'),)

type_subject_choice = (('л', 'Лекция'),
                       ('с', 'Семинар'),
                       ('лаб', 'Лабараторная'),
                       ('', 'Без типа'),)

frequency_choice = (('1 нед', '1 неделя'),
                    ('2 нед', '2 неделя'),
                    ('', 'Еженедельно'))


class Department(models.Model):  # Кафедра
    name = models.CharField(verbose_name="Имя кафедры", max_length=100)
    code = models.CharField(verbose_name='Код кафедры', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'


class Course(models.Model):  # Направление
    department = models.ForeignKey(Department, verbose_name='Кафедра', on_delete=models.CASCADE)

    name = models.CharField(verbose_name="Имя направления", max_length=100)
    code = models.CharField(verbose_name='Код направления', max_length=30)
    section = models.CharField(verbose_name='Профиль направления', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'


class Teacher(models.Model):  # Преподователь
    department = models.ForeignKey(Department, verbose_name='Кафедра', on_delete=models.CASCADE)

    surname = models.CharField(verbose_name='Фамилия', max_length=50)
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    patronymic = models.CharField(verbose_name='Отчество', max_length=50)
    position = models.CharField(verbose_name='Должность', max_length=100)  # TODO: мб создать еще одну модель

    def __str__(self):
        return '%s, %s' % (self.surname, self.first_name)

    class Meta:
        verbose_name = 'Преподователь'
        verbose_name_plural = 'Преподователи'


class AcademicDiscipline(models.Model):  # Дисциплина
    department = models.ForeignKey(Department, verbose_name='Кафедра', on_delete=models.CASCADE)
    course = models.ManyToManyField(Course, verbose_name='Направление')

    name = models.CharField(verbose_name='Имя дисцилины', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'


# TODO: мб связать с кафедрой
class Provision(models.Model):  # Софт(оборудование)
    name = models.CharField(verbose_name='Название софта(оборудования)', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Софт(оборудование)'
        verbose_name_plural = 'Софт(оборудование)'


class Subject(models.Model):  # Предмет
    department = models.ForeignKey(Department, verbose_name='Кафедра', on_delete=models.CASCADE)
    academic_discipline = models.ForeignKey(AcademicDiscipline, verbose_name='Дисциплина', on_delete=models.CASCADE)
    provision = models.ManyToManyField(Provision, verbose_name='Софт(оборудование)')

    type = models.CharField(verbose_name='Тип предмета', max_length=12, choices=type_subject_choice)

    def __str__(self):
        return '%s - %s' % (self.academic_discipline.name, self.type_subject.type)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Group(models.Model):  # Группа
    course = models.ForeignKey(Course, verbose_name='Направление', on_delete=models.CASCADE)

    name = models.CharField(verbose_name='Имя группы', max_length=50)
    the_size_of_the_group = models.IntegerField(verbose_name='Численность группы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Curriculum(models.Model):  # Учебный план
    subject = models.ForeignKey(Subject, verbose_name='Предмет', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE)

    number_of_hours = models.IntegerField(verbose_name='Количество часов')

    class Meta:
        verbose_name = 'Учебный план'
        verbose_name_plural = 'Учебные планы'


class WorkingHours(models.Model):  # Рабочее время преподавателя
    teacher = models.ForeignKey(Teacher, verbose_name='Преподователь', on_delete=models.CASCADE)

    day_of_the_week = models.CharField(verbose_name='День недели', max_length=12, choices=day_of_the_week_choice)
    the_daily_starting_time = models.TimeField(verbose_name='Начало рабочего дня', default="09:00:00")
    number_of_working_hours = models.TimeField(verbose_name='Количество рабочих часов', default="08:00:00")

    class Meta:
        verbose_name = 'Рабочее время преподавателя'
        verbose_name_plural = 'Рабочее время преподавателя'


class Classroom(models.Model):  # Аудитория
    department = models.ForeignKey(Department, verbose_name='Кафедра', null=True, on_delete=models.CASCADE)
    provision = models.ManyToManyField(Provision, verbose_name='Софт(оборудование)')

    auditorium_number = models.CharField(verbose_name='Номер аудитории', max_length=50)
    type = models.CharField(verbose_name='Тип аудитории', max_length=12, choices=type_subject_choice)
    capacity = models.IntegerField(verbose_name='Вместимость')
    housing = models.CharField(verbose_name='Корпус', max_length=12, choices=(('Тушино', 'Тушино'),
                                                                              ('Миуссы', 'Миуссы')))

    def __str__(self):
        return self.auditorium_number

    class Meta:
        verbose_name = 'Аудитория'
        verbose_name_plural = 'Аудитории'


class HalfLesson(models.Model):  # Промежуток полупары
    time_start = models.TimeField(verbose_name='Начало промедутка')
    time_end = models.TimeField(verbose_name='Окончание промедутка')

    def __str__(self):
        return '%s - %s' % (self.time_start, self.time_end)

    class Meta:
        verbose_name = 'Промежуток полупары'
        verbose_name_plural = 'Промежутки полупар'


class TableSchedule(models.Model):  # Общее расписание
    semester = models.IntegerField(verbose_name='Семестр')
    mod_date = models.DateField(verbose_name='Дата создания/модификации', default=datetime.date.today)

    def __str__(self):
        return 'Семестр %s (%s)' % (self.semester, self.mod_date)

    class Meta:
        verbose_name = 'Общее расписание'
        verbose_name_plural = 'Общее расписание'


class SpecificDate(models.Model):
    date = models.DateField(verbose_name='Дата')

    class Meta:
        verbose_name = 'Спец дата занятия'
        verbose_name_plural = 'Спец даты занятий'


class Schedule(models.Model):  # Расписание занятие в один день
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, verbose_name='Предмет', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, verbose_name='Преподователь', on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, verbose_name='Аудитория', on_delete=models.CASCADE)
    half_lesson = models.ManyToManyField(HalfLesson, verbose_name='Промежуток полупары')
    table_schedule = models.ForeignKey(TableSchedule, verbose_name='Общее расписание', on_delete=models.CASCADE)
    specific_date = models.ManyToManyField(SpecificDate, verbose_name='Спец даты занятий')

    frequency = models.CharField(verbose_name='Частота', max_length=12, choices=frequency_choice)
    day_of_the_week = models.CharField(verbose_name='День недели', max_length=12, choices=day_of_the_week_choice)

    class Meta:
        verbose_name = 'Расписание занятия'
        verbose_name_plural = 'Расписание занятий'


class Exam(models.Model):  # Экзамен
    academic_discipline = models.ForeignKey(AcademicDiscipline, verbose_name='Дисциплина', on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, verbose_name='Аудитория', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE)

    exam_date = models.DateField(verbose_name='День экзамена')

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'


class RestDay(models.Model):  # Выходной день
    table_schedule = models.ForeignKey(TableSchedule, verbose_name='Общее расписание', on_delete=models.CASCADE)

    name = models.CharField(verbose_name='Название выходного', max_length=50)
    rest_day = models.DateField(verbose_name='Дата выходного')

    class Meta:
        verbose_name = 'Выходной день'
        verbose_name_plural = 'Выходные дни'
