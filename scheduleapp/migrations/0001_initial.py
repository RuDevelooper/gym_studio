# Generated by Django 3.1.7 on 2021-03-14 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(default='static/img/team-01.jpg', upload_to='trainer_photos/')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание тренера')),
            ],
            options={
                'verbose_name': 'Тренер',
                'verbose_name_plural': 'Тренеры',
            },
        ),
        migrations.CreateModel(
            name='WorkoutType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('photo', models.ImageField(upload_to='media/', verbose_name='Изображение')),
                ('short_description', models.TextField(verbose_name='Краткое описание')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Вид тренировки',
                'verbose_name_plural': 'Виды тренировок',
            },
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('start_workout', models.TimeField(verbose_name='Начало тренировки')),
                ('workout_time', models.TimeField(verbose_name='Продолжительность тренировки')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workout', to='scheduleapp.trainer', verbose_name='Тренер')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workout', to='scheduleapp.workouttype', verbose_name='Вид тренировки')),
            ],
            options={
                'verbose_name': 'Тренировка',
                'verbose_name_plural': 'Тренировки',
            },
        ),
    ]