# Generated by Django 3.1.7 on 2021-03-14 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduleapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workout',
            options={'verbose_name': 'Занятие', 'verbose_name_plural': 'Расписание занятий'},
        ),
        migrations.AlterModelOptions(
            name='workouttype',
            options={'verbose_name': 'Вид занятий', 'verbose_name_plural': 'Виды занятий'},
        ),
        migrations.RemoveField(
            model_name='workouttype',
            name='short_description',
        ),
    ]