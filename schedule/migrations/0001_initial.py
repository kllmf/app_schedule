# Generated by Django 3.0.6 on 2020-05-28 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDiscipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auditorium_number', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Имя направления', max_length=100)),
                ('code', models.CharField(max_length=30)),
                ('section', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DayOfTheWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Имя кафедры', max_length=100)),
                ('code', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('the_size_of_the_group', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Course')),
            ],
        ),
        migrations.CreateModel(
            name='HalfLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Provision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TableSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
                ('mod_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('patronymic', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Department')),
            ],
        ),
        migrations.CreateModel(
            name='TypeClassroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TypeSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('the_daily_starting_time', models.TimeField()),
                ('number_of_working_hours', models.TimeField()),
                ('day_of_the_week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.DayOfTheWeek')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.AcademicDiscipline')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Department')),
                ('type_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.TypeSubject')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.TimeField()),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Classroom')),
                ('day_of_the_week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.DayOfTheWeek')),
                ('frequency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Frequency')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Group')),
                ('half_lesson', models.ManyToManyField(to='schedule.HalfLesson')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Subject')),
                ('table_schedule', models.ManyToManyField(to='schedule.TableSchedule')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='RestDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rest_day', models.DateField()),
                ('table_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.TableSchedule')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_date', models.DateField()),
                ('academic_discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.AcademicDiscipline')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Classroom')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_hours', models.IntegerField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Group')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Subject')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Department'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.Department'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='provision',
            field=models.ManyToManyField(to='schedule.Provision'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.TypeClassroom'),
        ),
        migrations.AddField(
            model_name='academicdiscipline',
            name='course',
            field=models.ManyToManyField(to='schedule.Course'),
        ),
        migrations.AddField(
            model_name='academicdiscipline',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Department'),
        ),
    ]
