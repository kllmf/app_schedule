# Generated by Django 3.0.6 on 2020-05-31 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workinghours',
            name='day_of_the_week',
            field=models.CharField(choices=[('Пн', 'Понедельник'), ('Вт', 'Вторник'), ('Ср', 'Среда'), ('Чт', 'Четверг'), ('Пт', 'Пятница'), ('Сб', 'Суббота')], max_length=11),
        ),
    ]